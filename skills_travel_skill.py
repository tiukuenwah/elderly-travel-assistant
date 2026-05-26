from utils.nlp_parser import NLPParser
from utils.itinerary_builder import ItineraryBuilder

class TravelSkill:
    def __init__(self):
        self.triggers = ["travel", "trip", "itinerary", "plan", "go out"]

    def match(self, text):
        for t in self.triggers:
            if t in text.lower():
                return True
        return False

    def execute(self, text):
        if not self.match(text):
            return {"code": 404, "message": "Not matched"}
        
        req = NLPParser.parse_request(text)
        builder = ItineraryBuilder()
        result = builder.build(req)
        
        output = (
            "✅ YOUR SENIOR TRAVEL PLAN IS READY\n\n"
            "ITINERARY:\n" + result["itinerary"] + "\n\n"
            "TODO LIST:\n" + result["todo"]
        )
        return {"code": 200, "content": output}

def run_skill(text):
    skill = TravelSkill()
    return skill.execute(text)