import requests


res_parse_list=[]

response=requests.get('https://www.olx.ua/d/uk/obyavlenie/operativna-pamyat-ddr2-1gb-IDOMg2F.html?search_reason=search%7Corganic')



response_text=response.text

response_paris=response_text.split('<h3')


for parse_elem_1 in response_paris:
    for parse_elem_2 in parse_elem_1.split('</h3>'):
        if parse_elem_2.endswith('.'):
            for llllll in response_paris:
                if 'class="css-yauxmy"' in llllll and '</h3>' in llllll:
                    after_tag = llllll.split('>', 1)[1]
                    price_text = after_tag.split('</h3>', 1)[0].strip()
                    real_price_in_UAH=float(price_text.split('грн.', 1)[0].strip())
                    print(f'{real_price_in_UAH} - ціна одної плашки оперативи в грн ')
                    B=float(input('Який в Вас бюджет?'))
                    if B<=0:
                        print("Ну якщо бюджет такий то допобачення")
                    else:
                        N=int(input('Скіки плашок оперативи Вам треба? Це якщо що DDR2'))
                        if N<=0:
                            print('А ну тоді все допобачення')
                        else:
                            if B/real_price_in_UAH<N:
                                print('Бюджету не хватає')
                            else:
                                price_for_buying=N*real_price_in_UAH
                                gold_price_per_gram=6000
                                gold_amount_per_plashka=0.05
                                gold_price_per_plashka=gold_amount_per_plashka*gold_price_per_gram
                                price_of_gold_per_all=gold_price_per_plashka*N
                                print(f'{price_of_gold_per_all} грн Ви отримаєте з золота цієї оперативи, а заплатили Ви {price_for_buying}')
                                if price_of_gold_per_all > price_for_buying:
                                    print(f"Ну Ви в плюсі на {price_of_gold_per_all-price_for_buying} грн, молодець")
                                elif price_of_gold_per_all==price_for_buying:
                                    print('Ну хоть в 0 вийшли')
                                else: print(f'Ви успішно профукали {price_for_buying-price_of_gold_per_all} грн, сумно')



