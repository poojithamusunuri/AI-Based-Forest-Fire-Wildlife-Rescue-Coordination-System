class PEAS:

    performance = (
        "Minimize forest fire impact "
        "and wildlife casualties"
    )

    environment = (
        "Dynamic forest fire and "
        "wildlife rescue environment"
    )

    actuators = [
        "Wildlife Rescue Team",
        "Drone Monitoring Unit",
        "Fire Response Vehicle"
    ]

    sensors = [
        "Weather Sensors",
        "Drone Surveillance",
        "Wildlife Monitoring Data"
    ]

    @staticmethod
    def display():
        print("\n=== PEAS MODEL ===")
        print("Performance:", PEAS.performance)
        print("Environment:", PEAS.environment)
        print("Actuators:", ", ".join(PEAS.actuators))
        print("Sensors:", ", ".join(PEAS.sensors))