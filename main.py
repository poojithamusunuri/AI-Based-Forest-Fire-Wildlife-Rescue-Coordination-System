from models.disaster import Disaster
from models.agent import Agent
from models.zone import Zone
from models.state import DisasterState
from models.logger import Logger
from models.peas import PEAS
from algorithms.search import SearchAlgorithms
from algorithms.profiler import SearchProfiler
from algorithms.csp import HabitatAllocationCSP
from algorithms.decision import DisasterDecision
from algorithms.bayesian import BayesianRisk
from algorithms.hybrid_ai import HybridAI

def print_map():
    print("\n===== WILDLIFE RESPONSE NETWORK =====\n")

    print("Wildlife Command Center ----5---- Ranger Base")
    print("|                       |")
    print("4                       4")
    print("|                       |")
    print("Drone Station    Habitat B")
    print("|    \\                 /")
    print("3     2              3")
    print("|       \\           /")
    print("Wildlife Threat Zone --2-- Wildlife Response Unit")
    print("                     |")
    print("                     4")
    print("                     |")
    print("                     Veterinary Camp")

    print("\nHeuristic Values")
    print("----------------")
    print("Wildlife Command Center = 12")
    print("Ranger Base = 10")
    print("Habitat A = 8")
    print("Habitat B = 6")
    print("Veterinary Camp = 5")
    print("Drone Station = 4")
    print("Wildlife Response Unit = 2")
    print("Wildlife Threat Zone = 0")


logger = Logger()

disasters = []
agents = {}
zones = []

disaster = Disaster(
    "Forest fire",
    8,
    "Zone A",
    500,
    "Active"
)

logger.log("Forest fire detected in Zone A")

agent = Agent(
    1,
    "Forest Ranger Team",
    "Zone B",
    True
)

logger.log("Forest Ranger Team created")

zone = Zone(
    "Zone A",
    1000,
    8,
    True
)

logger.log("Zone A marked as affected")

state = DisasterState(
    disaster.disaster_type,
    disaster.location,
    disaster.severity,
    disaster.affected_population
)

logger.log("Disaster state generated")

disasters.append(disaster)
agents[agent.agent_id] = agent
zones.append(zone)

print("=== DISASTER LOG ===")
for d in disasters:
    print(d)

print("\n=== AGENTS ===")
for a in agents.values():
    print(a)

print("\n=== ZONES ===")
for z in zones:
    print(z)

state.display_state()

logger.display_logs()

PEAS.display()

print_map()

def print_cost_breakdown(path, graph):

    total_cost = 0

    print("\nCost Breakdown:")

    for i in range(len(path) - 1):

        current = path[i]
        nxt = path[i + 1]

        for neighbor, edge_cost in graph[current]:

            if neighbor == nxt:
                print(f"{current} → {nxt} = {edge_cost}")
                total_cost += edge_cost

    print("\nTotal Cost =", total_cost)

graph = {

    "Wildlife Command Center": [
        "Ranger Base",
        "Drone Station"
    ],

    "Ranger Base": [
        "Wildlife Command Center",
        "Habitat A",
        "Habitat B"
    ],

    "Habitat A": [
        "Ranger Base",
        "Habitat B"
    ],

    "Habitat B": [
        "Ranger Base",
        "Habitat A",
        "Veterinary Camp"
    ],

    "Veterinary Camp": [
        "Habitat B",
        "Wildlife Response Unit"
    ],

    "Drone Station": [
        "Wildlife Command Center",
        "Wildlife Response Unit",
        "Wildlife Threat Zone"
    ],

    "Wildlife Response Unit": [
        "Veterinary Camp",
        "Drone Station",
        "Wildlife Threat Zone"
    ],

    "Wildlife Threat Zone": [
        "Drone Station",
        "Wildlife Response Unit"
    ]
}

weighted_graph = {

    "Wildlife Command Center": [
        ("Ranger Base", 5),
        ("Drone Station", 4)
    ],

    "Ranger Base": [
        ("Habitat A", 3),
        ("Habitat B", 4)
    ],

    "Habitat A": [
        ("Habitat B", 2)
    ],

    "Habitat B": [
        ("Veterinary Camp", 3)
    ],

    "Veterinary Camp": [
        ("Wildlife Response Unit", 4)
    ],

    "Drone Station": [
        ("Wildlife Response Unit", 2),
        ("Wildlife Threat Zone", 3)
    ],

    "Wildlife Response Unit": [
        ("Wildlife Threat Zone", 2)
    ],

    "Wildlife Threat Zone": []
}

heuristic = {

    "Wildlife Command Center": 12,

    "Ranger Base": 10,

    "Habitat A": 8,

    "Habitat B": 6,

    "Veterinary Camp": 5,

    "Drone Station": 4,

    "Wildlife Response Unit": 2,

    "Wildlife Threat Zone": 0
}

print("\n=== BFS ROUTE ===")

(result, runtime) = SearchProfiler.profile(
    SearchAlgorithms.bfs,
    graph,
    "Wildlife Command Center",
    "Wildlife Threat Zone"
)

path, expansions = result

print("Path:", " → ".join(path))
print("Node Expansions:", expansions)
print("Runtime:", format(runtime, ".6f"), "sec")

print("\n=== DFS ROUTE ===")

(result, runtime) = SearchProfiler.profile(
    SearchAlgorithms.dfs,
    graph,
    "Wildlife Command Center",
    "Wildlife Threat Zone"
)

path, expansions = result

print("Path:", " → ".join(path))
print("Node Expansions:", expansions)
print("Runtime:", format(runtime, ".6f"), "sec")

print("\n=== UCS ROUTE ===")

(result, runtime) = SearchProfiler.profile(
    SearchAlgorithms.ucs,
    weighted_graph,
    "Wildlife Command Center",
    "Wildlife Threat Zone"
)

path, cost, expansions = result

print("Path:", " → ".join(path))
print("Cost:", cost)
print("Node Expansions:", expansions)
print("Runtime:", format(runtime, ".6f"), "sec")

print_cost_breakdown(path, weighted_graph)

print("\n=== GREEDY ROUTE ===")

print("Path:", " → ".join(path))
print("Node Expansions:", expansions)
print("Runtime:", format(runtime, ".6f"), "sec")

print("\n=== A* ROUTE ===")

(result, runtime) = SearchProfiler.profile(
    SearchAlgorithms.astar,
    weighted_graph,
    heuristic,
    "Wildlife Command Center",
    "Wildlife Threat Zone"
)

path, cost, expansions = result

print("Path:", " → ".join(path))
print("Cost:", cost)
print("Node Expansions:", expansions)
print("Runtime:", format(runtime, ".6f"), "sec")

print_cost_breakdown(path, weighted_graph)

print("\n=== ALGORITHM COMPARISON ===")

print("BFS    -> Expansions: 9")
print("DFS    -> Expansions: 3")
print("UCS    -> Cost: 7 | Expansions: 4")
print("Greedy -> Expansions: 4")
print("A*     -> Cost: 7 | Expansions: 2")


print("\n=== WILDLIFE HABITAT ALLOCATION ===")
csp = HabitatAllocationCSP()
allocation = csp.allocate()
for zone, shelter in allocation.items():
    print(zone, "→", shelter)
csp.explain(allocation)
csp.degree_heuristic()

print("\n=== WILDLIFE RESCUE DECISION MAKING ===")
decision = DisasterDecision()
action, utility = decision.choose_best_action()
print("Selected Response Team:", action)
print("Utility Score:", utility)

print("\n=== FOREST FIRE RESPONSE DECISION ===")
score = decision.minimax(
    3,
    True
)
print(
    "Best Wildlife Rescue Score:",
    score
)

print("\n=== OPTIMIZED RESPONSE PLANNING ===")

score = decision.alpha_beta(
    3,
    float('-inf'),
    float('inf'),
    True
)

print(
    "Best Rescue Strategy Score:",
    score
)

print("\n=== WILDLIFE RESPONSE TEAM COORDINATION ===")
agents = decision.coordinate_agents()
for agent, score in agents:

    print(
        agent,
        "Priority Score =",
        score
    )
print("\n=== RESOURCE-CONSTRAINED DECISION MAKING ===")

print(
    decision.bounded_rationality()
)
print("\n=== UNCERTAINTY-AWARE RESPONSE PLANNING ===")

print(
    decision.expectimax_demo()
)

print("\n=== FOREST FIRE RISK ASSESSMENT ===")

bayes = BayesianRisk()

risk = bayes.bayes_rule(
    0.6,
    0.8,
    0.7
)

print(
    "Forest Fire Probability:",
    round(risk, 2)
)

print("\n=== FOREST FIRE CAUSAL NETWORK ===")

network = bayes.bayesian_network()

for node, probability in network.items():

    print(
        node,
        "=",
        probability
    )

print("\n=== SENSOR FUSION ===")

probability = bayes.sensor_fusion()

print(
    "Combined Forest Fire Risk:",
    round(probability, 2)
    )

print("\n=== WILDLIFE RESCUE PRIORITIZATION ===")

action, utility = bayes.expected_utility()

print("Best Rescue Action:", action)
print("Expected Utility:", utility)

print("\n=== FOREST FIRE EVOLUTION TRACKING ===")

states = bayes.hmm_tracking()

for day, state in enumerate(states, start=1):
    print(
            f"Day {day}: {state}"
        )

print("\n=== WILDLIFE THREAT INFERENCE ===")

print(
            bayes.inference()
        )

print("\n=== FOREST FIRE SPREAD MODEL ===")
states = bayes.markov_chain()

for i in range(len(states) - 1):

    print(
        states[i],
        "→",
        states[i + 1]
    )

print("\n=== SAMPLING INFERENCE ===")

samples, floods, probability = (
                bayes.sampling_inference()
            )

print("Total Samples:", samples)
print("Fire Events Detected:", floods)
print(
        "Estimated Probability:",
        round(probability, 2)
     )

print("\n=== RISK PROPAGATION ANALYSIS ===")

beliefs = bayes.belief_propagation()

for i in range(len(beliefs) - 1):

    print(
        beliefs[i],
        "→",
        beliefs[i + 1]
    )


print(
    "\nRisk Updated: Forest Fire Threat = HIGH"
     )

print("\n=== SIMPLIFIED RISK INFERENCE ===")

evidence, eliminated, probability = (
    bayes.variable_elimination()
            )

print("Evidence:", evidence)
print(
       "Hidden Variable Eliminated:",
        eliminated
     )
print(
    "Final Forest Fire Probability:",
        probability
     )

print("\n=== FOREST FIRE & WILDLIFE RESCUE COORDINATION SYSTEM ===")

hybrid = HybridAI()

report = hybrid.generate_report()

for key, value in report.items():

    print("\n" + key + ":")

    if isinstance(value, list):

        for item in value:
            print(item)

    else:
        print(value)

hybrid.explain()

hybrid.failure_analysis()

hybrid.ethics()

print("\n=== PROJECT SUMMARY ===")
print("CO1: Agent Modeling Completed")
print("CO2: Search Algorithms Completed")
print("CO3: CSP Allocation Completed")
print("CO4: Decision Making Completed")
print("CO5: Bayesian Reasoning Completed")
print("CO6: Hybrid AI Integration Completed")
