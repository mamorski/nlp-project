import pandas as pd
pathToFile = "C:\\Users\\nadav\\Downloads\\results.csv"
fileHandler = pd.read_csv(pathToFile)
keyword = None
whichBestResult = None
modelsMap = {"IMDB": {"XLNET Cased": {"best result Test": 0, "best result Translated": 0, "bestParamsTest": [], "bestParamsTranslated": []}, "Bert Cased": {"best result Test": 0, "best result Translated": 0, "bestParamsTest": [], "bestParamsTranslated": []}, "Bert Uncased": {"best result Test": 0, "best result Translated": 0, "bestParamsTest": [], "bestParamsTranslated": []}}, "Amazon": {"Yes": {"XLNET Cased": {"best result Test": 0, "best result Translated": 0, "best result IMDB": 0, "bestParamsTest": [], "bestParamsTranslated": [], "bestParamsIMDB": []}, "Bert Cased": {"best result Test": 0, "best result Translated": 0, "best result IMDB": 0, "bestParamsTest": [], "bestParamsTranslated": [], "bestParamsIMDB": []}, "Bert Multilingual Cased": {"best result Test": 0, "best result Translated": 0, "best result IMDB": 0, "bestParamsTest": [], "bestParamsTranslated": [], "bestParamsIMDB": []}, "Bert Multilingual Uncased": {"best result Test": 0, "best result Translated": 0, "best result IMDB": 0, "bestParamsTest": [], "bestParamsTranslated": [], "bestParamsIMDB": []}, "Bert Uncased": {"best result Test": 0, "best result Translated": 0, "best result IMDB": 0, "bestParamsTest": [], "bestParamsTranslated": [], "bestParamsIMDB": []}}, "No": {"XLNET Cased": {"best result Test": 0, "best result Translated": 0, "best result IMDB": 0, "bestParamsTest": [], "bestParamsTranslated": [], "bestParamsIMDB": []}, "Bert Cased": {"best result Test": 0, "best result Translated": 0, "best result IMDB": 0, "bestParamsTest": [], "bestParamsTranslated": [], "bestParamsIMDB": []}, "Bert Uncased": {"best result Test": 0, "best result Translated": 0, "best result IMDB": 0, "bestParamsTest": [], "bestParamsTranslated": [], "bestParamsIMDB": []}, "Bert Multilingual Cased": {"best result Test": 0, "best result Translated": 0, "best result IMDB": 0, "bestParamsTest": [], "bestParamsTranslated": [], "bestParamsIMDB": []}, "Bert Multilingual Uncased": {"best result Test": 0, "best result Translated": 0, "best result IMDB": 0, "bestParamsTest": [], "bestParamsTranslated": [], "bestParamsIMDB": []}}}}
for line in fileHandler.values:
    if "Multilingual" in line[0]:
        currModel = "".join(line[0].strip().split(' ')[0].strip() + ' ' + line[0].strip().split(' ')[1].strip() + ' ' + line[0].strip().split(' ')[2].strip())
    else:
        currModel = "".join(line[0].strip().split(' ')[0].strip() + ' ' + line[0].strip().split(' ')[1].strip())
    dataset = line[1].strip()
    transOrTest = line[2].strip()
    if "Translated" in transOrTest:
        whichBestResult = "Translated"
    elif "IMDB" in transOrTest and dataset != "IMDB":
        whichBestResult = "IMDB"
    else:
        whichBestResult = "Test"
    F1Score = float(line[3])
    N = str(line[4]).strip()
    M = str(line[5]).strip()
    if dataset == "IMDB":
        if modelsMap[dataset][currModel][f"best result {whichBestResult}"] < F1Score:
            modelsMap[dataset][currModel][f"best result {whichBestResult}"] = F1Score
            if "Translated" in transOrTest:
                modelsMap[dataset][currModel]["bestParamsTranslated"] = [currModel, '-', dataset, "Amazon Translated", str(F1Score).strip(), N, M]
            else:
                modelsMap[dataset][currModel]["bestParamsTest"] = [currModel, '-', dataset, "IMDB Test", str(F1Score).strip(), N, M]
    else:
        if "without" in line[0]:
            keyword = "No"
        else:
            keyword = "Yes"

        if modelsMap[dataset][keyword][currModel][f"best result {whichBestResult}"] < F1Score:
            modelsMap[dataset][keyword][currModel][f"best result {whichBestResult}"] = F1Score
            if "Translated" in transOrTest:
                modelsMap[dataset][keyword][currModel]["bestParamsTranslated"] = [currModel, keyword, dataset, "Amazon Translated", str(F1Score).strip(), N, M]
            elif "IMDB" in transOrTest:
                modelsMap[dataset][keyword][currModel]["bestParamsIMDB"] = [currModel, keyword, dataset, "IMDB Test", str(F1Score).strip(), N, M]
            else:
                modelsMap[dataset][keyword][currModel]["bestParamsTest"] = [currModel, keyword, dataset, "Amazon Test", str(F1Score).strip(), N, M]


for dataset, maps in modelsMap.items():
    if dataset == "IMDB":
        for model, newMaps in maps.items():
            print(" & ".join(newMaps['bestParamsTest'])+ "\\\\")
            print(" & ".join(newMaps['bestParamsTranslated']) + "\\\\")
    else:
        for keyword in ["Yes", "No"]:
            for model, newMaps in maps[keyword].items():
                print(" & ".join(newMaps['bestParamsTest']) + "\\\\")
                print(" & ".join(newMaps['bestParamsTranslated']) + "\\\\")
                if newMaps['bestParamsIMDB']:
                    print(" & ".join(newMaps['bestParamsIMDB']) + "\\\\")
