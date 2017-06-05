def result(request):
    adult_num=request.POST.get("adult_num")
    kid_num=request.POST.get("kid_num")
    depday=request.POST.get("depday")
    arrday=request.POST.get("arrday")
    airports = []
    LHR=request.POST.get("LHR")
    airports.extend([LHR])
    CDG=request.POST.get("CDG")
    airports.extend([CDG])
    FCO=request.POST.get("FCO")
    airports.extend([FCO])
    TXL=request.POST.get("TXL")
    airports.extend([TXL])
    MAD=request.POST.get("MAD")
    airports.extend([MAD])
    air=['ICN']
    for airport in airports:
        if airport != None:
            air.append(str(airport))
            print(air) 
    # result = tsp(air)
    # a=1
    # tsp(a)
    # b=tsp(a)
    compact(air, arrday)
    # a=str()
    # for i in range(len(result_air)):
    #   a=a+str(i)
    print("new",result_air)
    # for i in range(len(result_dep)):
    #   if result_dep[i]<10:
    #       result_dep[i]=str('0')+str(result_dep[i])
    #   else:
    #       result_dep[i]=str(result_dep[i])
    response = [0]*(len(result_dep))
    api_key= [0]*(len(result_dep))
    url=[0]*(len(result_dep))
    headers=[0]*(len(result_dep))
    params=[0]*(len(result_dep))
    api_key = "AIzaSyDiYhxOy8UR29FtgCQHsZz_7yxRkIrVK_E"
    url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" + api_key
    headers = {'content-type': 'application/json'}
    prices=[]
    stops=[]
    carriers=[]
    carriers_2=[]
    for i in range(len(result_dep)):
        params = {
            "request": {
                    "slice": [
                        {
                        "origin": result_air[i],
                        "destination": result_air[i+1],
                        "date": "2017-07-" + result_dep[i],
                        "maxStops": 1,
                        "maxConnectionDuration": 3000,
                    }
                ],
                "passengers": {
                    "adultCount": 1,
                    "childCount": 0,
                },
                "solutions": 20,
                "refundable": False,
                "saleCountry": "US",
            }
        }
        response = requests.post(url, data=json.dumps(params), headers=headers)
        data = response.json()
        price=[0]*3
        stop=[0]*3
        Carrier=[0]*3
        Carriersss=[0]*3
        for j in range(3):
            price[j] = data["trips"]["tripOption"][j]["saleTotal"]
            stop[j] = data['trips']['tripOption'][j]['slice'][0]['segment'][0].get('connectionDuration', 'Direct')
            Carrier[j] = data["trips"]["tripOption"][j]["slice"][0]["segment"][0]["flight"]["carrier"]+data["trips"]["tripOption"][0]["slice"][0]["segment"][0]["flight"]["number"],
            Carriersss[j]= data["trips"]["data"]["carrier"][j]["name"]
            prices.append(str(price[j]))
            stops.append(stop[j])
            carriers.append(Carrier[j])
            carriers_2.append(Carriersss[j])
    print(prices)
    real_price=[]
    for i in range(18):
        real_price.append(str("price")+str(i))
#이름 자동 생성
    real_stop=[]
    for i in range(18):
        real_stop.append(str("stop")+str(i))
    real_carrier=[]
    for i in range(18):
      real_carrier.append(str("carrier")+str(i))
    real_carrier2=[]
    for i in range(18):
      real_price.append(str("carrier2_")+str(i))
    for i in range(len(real_price)-len(prices)):
        prices.append(0)
        stops.append(0)
        carriers.append(0)
        carriers_2.append(0)
#
    for i in zip(real_price,prices,real_stop,stops,real_carrier,carriers,real_carrier2,carriers_2):
        if i[1] != 0:
            #globals: string을 변수로
            globals()[i[0]]=i[1][3:]
            #exec("%s = %s" % (i[0],i[1][3:]))
            globals()[i[2]]=i[3]
            # globals()[i[4]]=i[5]
            # globals()[i[6]]=i[7]
        else:
            exec("%s = %s" % (i[0],i[1]))
            exec("%s = %s" % (i[2],i[3]))
            # exec("%s = %s" % (i[3],i[1]))
            # exec("%s = %s" % (i[4],i[1]))
    
    price_t1=[22,34,55]
    price_t2=0  
    prices1=[price0,price1,price2,price_t1]
    prices2=[price3,price4,price5,price_t1]
    prices3=[price6,price7,price8,price_t1]
    prices4=[price9,price10,price11,price_t2]
    prices5=[price12,price13,price14,price_t2]
    prices6=[price15,price16,price17,price_t2]
    stops1=[stop0,stop1,stop2,price_t1]
    stops2=[stop3,stop4,stop5,price_t1]
    stops3=[stop6,stop7,stop8,price_t1]
    stops4=[stop9,stop10,stop11,price_t2]
    stops5=[stop12,stop13,stop14,price_t2]
    stops6=[stop15,stop16,stop17,price_t2]
    carriers1=[carrier0,carrier1,carrier2,price_t1]
    carriers2=[carrier3,carrier4,carrier5,price_t1]
    carriers3=[carrier6,carrier7,carrier8,price_t1]
    carriers4=[carrier9,carrier10,carrier11,price_t2]
    carriers5=[carrier12,carrier13,carrier14,price_t2]
    carriers6=[carrier15,carrier16,carrier17,price_t2]
    carriers2_1=[carrier2_0,carrier2_1,carrier2_2,price_t1]
    carriers2_2=[carrier2_3,carrier2_4,carrier2_5,price_t1]
    carriers2_3=[carrier2_6,carrier2_7,carrier2_8,price_t1]
    carriers2_4=[carrier2_9,carrier2_10,carrier2_11,price_t2]
    carriers2_5=[carrier2_12,carrier2_13,carrier2_14,price_t2]
    carriers2_6=[carrier2_15,carrier2_16,carrier2_17,price_t2]
            
    kkk=[zip(prices1,stops1),zip(prices2,stops2),zip(prices3,stops3),zip(prices4,stops4),zip(prices5,stops5),zip(prices6,stops6)]
    # totalcost=0
    # for k in range(len(result_air)-1):
        # totalcost = totalcost+string([3*k][3:])
    return render(request, 'pages/result.html', {"adult_num": adult_num,
                                                 "kid_num": kid_num,
                                                 "depday": depday,
                                                 "arrday": arrday,
                                                 "LHR": LHR,
                                                 # 'obj': models.Crawldata.objects.all()[:5],
                                                 "result_st": result_st,
                                                 # "totalcost": totalcost,
                                                 # #traveling city
                                                 # "city1": tsp.new_airport[0],
                                                 # "city2": tsp.new_airport[1],
                                                 # "city3": tsp.new_airport[2],
                                                 # "city4": tsp.new_airport[3],
                                                 # "city5": tsp.new_airport[4],
                                                 # #traveling day
                                                 # "date1": tsp.new_departure[0],
                                                 # "date2": tsp.new_departure[1],
                                                 # "date3": tsp.new_departure[2],
                                                 # "date4": tsp.new_departure[3],
                                                 # "date5": tsp.new_departure[4],
                                                 #stop or direct
                                                 "stop": stops,
                                                 "prices": prices,
                                                 "carrier": carriers,
                                                 "carriers": carriers_2,
                                                 "kkk":kkk
                                    
                                                 #"price_test":price_test
                                                 })