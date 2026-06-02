class DisasterDecision:

    def __init__(self):

        self.actions = {

            "Wildlife Rescue Team": 90,

            "Veterinary Unit": 85,

            "Drone Monitoring Team": 70
        }

    def choose_best_action(self):

        best_action = max(
            self.actions,
            key=self.actions.get
        )

        utility = self.actions[best_action]

        return best_action, utility

    def minimax(self, depth, maximizing):

        if depth == 0:
            return 50

        if maximizing:

            return max(
                self.minimax(
                    depth - 1,
                    False
                ),
                self.minimax(
                    depth - 1,
                    False
                ) + 10
            )

        else:

            return min(
                self.minimax(
                    depth - 1,
                    True
                ),
                self.minimax(
                    depth - 1,
                    True
                ) - 10
            )

    def alpha_beta(
            self,
            depth,
            alpha,
            beta,
            maximizing):

        if depth == 0:
            return 50

        if maximizing:

            value = float('-inf')

            for _ in range(2):

                value = max(
                    value,
                    self.alpha_beta(
                        depth - 1,
                        alpha,
                        beta,
                        False
                    )
                )

                alpha = max(alpha, value)

                if beta <= alpha:
                    print("Pruning Branch")
                    break

            return value

        else:

            value = float('inf')

            for _ in range(2):

                value = min(
                    value,
                    self.alpha_beta(
                        depth - 1,
                        alpha,
                        beta,
                        True
                    )
                )

                beta = min(beta, value)

                if beta <= alpha:
                    print("Pruning Branch")
                    break

            return value

    def coordinate_agents(self):

        agents = {

            "Wildlife Rescue Team": 90,

            "Veterinary Unit": 85,

            "Drone Monitoring Team": 70,

            "Fire Response Unit": 80
        }

        sorted_agents = sorted(
            agents.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return sorted_agents

    def bounded_rationality(self):

        return (
            "Deploy Top 2 Wildlife "
            "Response Units Only"
        )

    def expectimax_demo(self):

        return (
            "Expected outcome calculated "
            "using probabilistic disaster scenarios."
        )