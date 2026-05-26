from utils.city_data import CITY_DATA

class ItineraryBuilder:
    def build(self, req):
        city = req.get("city")
        if not city or city not in CITY_DATA:
            return {"error": "City not supported"}

        data = CITY_DATA[city]
        lines = []
        todo = []

        lines.append("=== SENIOR FRIENDLY ITINERARY ===")
        lines.append(f"City: {city} | Days: {req['days']} | Style: {req['style']}")
        lines.append("")

        lines.append("08:00 Wake up - take medicine - drink water")
        todo.append("[ ] 08:00 Wake up, medicine, water")

        lines.append("09:00 Depart by subway/bus")
        todo.append("[ ] 09:00 Depart")

        spot = data["spots"][0]
        lines.append(f"09:30 Visit {spot['name']} | {spot['walk']} | {spot['transit']}")
        lines.append(f"Guide: {spot['guide']}")
        todo.append(f"[ ] Visit {spot['name']}")

        lines.append("11:30 Lunch at local cheap restaurant")
        todo.append("[ ] Lunch")

        lines.append("12:30 Rest break")
        todo.append("[ ] Rest")

        lines.append("16:00 Return home safely")
        todo.append("[ ] Return home")

        lines.append("")
        lines.append(f"Nearby hospital: {spot['hospital']}")
        lines.append(f"Accommodation: {data['hotel']['name']} (¥{data['hotel']['price']})")
        lines.append(f"Share to family: {data['share_msg']}")

        return {
            "itinerary": "\n".join(lines),
            "todo": "\n".join(todo)
        }