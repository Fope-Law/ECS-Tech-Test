medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]

def createMedalTable(results):
    # Use the results object above to create a medal table
    # The winner gets 3 points, second place 2 points and third place 1 point
    position_points = {
    1: 3,
    2: 2,
    3: 1 }

    medalTable = {}
    
    for result in results:
        for team in result["podium"]:
            tmp = team.split(".")
            tmp_position = tmp[0]
            tmp_team = tmp[1]  
            
            if tmp_team in medalTable:
                medalTable[tmp_team] += position_points[int(tmp_position)]
            else:
                medalTable[tmp_team] = position_points[int(tmp_position)]
 
    return medalTable


def test_function():
    #This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable