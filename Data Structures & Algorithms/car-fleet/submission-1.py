class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_car = sorted(zip(position, speed), reverse=True)

        arrive = [
            (target - car[0]) / car[1] for car in sorted_car
        ]
        fleet = []
        for f in arrive:
            if not fleet or f > fleet[-1]:
                fleet.append(f)

        return len(fleet)