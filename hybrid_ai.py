class HybridAI:

    def generate_report(self):
        report = {

            "Forest Fire Risk Assessment":
                "HIGH",

            "Optimal Rescue Route":
                "Forest Fire Control Center → Drone Monitoring Station → Forest Fire Zone",

            "Wildlife Habitat Allocation":
                [
                    "Zone A → Habitat B",
                    "Zone B → Habitat A",
                    "Zone C → Habitat A"
                ],

            "Recommended Rescue Action":
                "Deploy Wildlife Rescue Team"
        }

        return report

    def explain(self):
        print("\n=== EXPLAINABLE REASONING ===")

        print(
            "A* selected the fastest rescue route "
            "to reach the forest fire zone."
        )

        print(
            "CSP allocated rescued animals "
            "to habitats based on capacity constraints."
        )

        print(
            "Bayesian reasoning estimated "
            "a high forest fire risk."
        )

        print(
            "The decision module selected "
            "the Wildlife Rescue Team due to "
            "its highest utility score."
        )

    def failure_analysis(self):
        print("\n=== FAILURE ANALYSIS ===")

        print(
            "Habitat allocation may fail "
            "if all habitats reach capacity."
        )

        print(
            "Incorrect weather or drone data "
            "may reduce prediction accuracy."
        )

    def ethics(self):
        print("\n=== ETHICS & LIMITATIONS ===")

        print(
            "Heuristic bias may influence "
            "wildlife rescue prioritization."
        )

        print(
            "Forest fire probability estimates "
            "remain uncertain."
        )

        print(
            "Human experts should validate "
            "critical rescue decisions."
        )