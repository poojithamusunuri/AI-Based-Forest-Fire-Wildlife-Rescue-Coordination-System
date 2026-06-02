class HabitatAllocationCSP:

    def __init__(self):

        self.zones = {
            "Zone A": 120,
            "Zone B": 80,
            "Zone C": 40
        }

        self.habitats = {
            "Habitat A": 120,
            "Habitat B": 150
        }

    def is_valid(self, habitat, animals, remaining_capacity):

        return remaining_capacity[habitat] >= animals

    def forward_check(self, remaining_capacity):
        print("Forward Checking...")

        available = False

        for capacity in remaining_capacity.values():

            if capacity > 0:
                available = True

        return available

    def select_mrv_zone(
            self,
            zones,
            allocation):

        unassigned = []

        for zone in zones:

            if zone not in allocation:
                unassigned.append(zone)

        return max(
            unassigned,
            key=lambda z: self.zones[z]
        )

    def backtrack(
            self,
            zones,
            allocation,
            remaining_capacity):

        if len(allocation) == len(zones):
            return allocation

        zone = self.select_mrv_zone(
            zones,
            allocation
        )

        print(f"MRV Selected: {zone}")

        people = self.zones[zone]

        ordered_habitats = self.lcv_order(
            people,
            remaining_capacity
        )

        print("LCV Order:", ordered_habitats)

        for habitat in ordered_habitats:

            if self.is_valid(
                    habitat,
                    people,
                    remaining_capacity):
                print(f"Relocating {zone} -> {habitat}")
                allocation[zone] = habitat

                remaining_capacity[habitat] -= people

                if self.forward_check(remaining_capacity):

                    result = self.backtrack(
                        zones,
                        allocation,
                        remaining_capacity
                    )

                    if result:
                        return result

                print(f"Backtracking {zone}")
                remaining_capacity[habitat] += people

                del allocation[zone]

        return None

    def allocate(self):

        zones = list(self.zones.keys())

        return self.backtrack(
            zones,
            {},
            self.habitats.copy()
        )

    def explain(self, allocation):

        print("\nHabitat Allocation Explanation:")

        for zone, habitat in allocation.items():

            if habitat == "No Habitat Available":

                print(
                    f"{zone} could not be relocated "
                    f"because all habitats were full."
                )

            else:

                print(
                    f"{zone} relocated to {habitat}"
                )

    def degree_heuristic(self):

        print("\nDegree Heuristic:")

        for zone in self.zones:
            print(
                zone,
                "affects",
                len(self.habitats),
                "possible habitats"
            )

    def lcv_order(
            self,
            people,
            remaining_capacity):

        habitats = list(self.habitats.keys())

        habitats.sort(
            key=lambda h:
            remaining_capacity[h] - people,
            reverse=True
        )

        return habitats