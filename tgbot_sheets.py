# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 14:19:43 2022

@author: Machine
"""
import os
import datetime
import telebot
import gspread
import pandas as pd
import matplotlib.pyplot as plt
from telebot import types
import numpy as np


def remove_date_duplicates (data_frame):
    #data_frame["Timestamp"] = pd.to_datetime(data_frame["Timestamp"], format  = "%d.%m.%Y %H:%M:%S", dayfirst= True)
    del data_frame['Timestamp']
    #pd.to_datetime(data_frame["Date"],  dayfirst = True)
    data_frame["Date"] = pd.to_datetime(data_frame["Date"], format = "%d.%m.%Y", dayfirst = True)
    data_frame = data_frame.sort_values(by = "Date") 
    print("Найдено дубликатов по дате:" + str(data_frame.Date.duplicated().sum()))
    return (data_frame.drop_duplicates(subset = "Date", keep = 'last'))
 

   
#Вывод: датафрейм с датой последнего отчета        



    

#Закидывание гугл докс в дфы:
#atmosfera

worksheet_atmosfera = sh.get_worksheet(0)
df_raw_atmosfera = pd.DataFrame(worksheet_atmosfera.get_all_records())
atmosfera_df = remove_date_duplicates(df_raw_atmosfera)
#frade_km

worksheet_frade_km = sh.get_worksheet(0)
df_raw_frade_km = pd.DataFrame(worksheet_frade_km.get_all_records())
df_raw_frade_km = df_raw_frade_km[df_raw_frade_km['Shop'] == 'Фраде Молл']
frade_km_df = remove_date_duplicates(df_raw_frade_km)
#frade_m
sh = gc.open_by_key("1SJQIBfGM_sKGK_hgVPM3hzKx1s_fspjGa_9zHL7Y4Oc")
worksheet_frade_km = sh.get_worksheet(0)
df_raw_frade_m = pd.DataFrame(worksheet_frade_km.get_all_records())
df_raw_frade_m = df_raw_frade_m[df_raw_frade_m['Shop'] == 'Фраде МЕГА']
frade_m_df = remove_date_duplicates(df_raw_frade_m)


worksheet_frade_km = sh.get_worksheet(0)
df_raw_fch_km = pd.DataFrame(worksheet_frade_km.get_all_records())
df_raw_fch_km = df_raw_fch_km[df_raw_fch_km['Shop'] == 'ФЧ МОЛЛ']
fch_km_df = remove_date_duplicates(df_raw_fch_km)
#fchm
worksheet_frade_km = sh.get_worksheet(0)
raw_fch_m_df = pd.DataFrame(worksheet_frade_km.get_all_records())
raw_fch_m_df = raw_fch_m_df[raw_fch_m_df['Shop'] == 'ФЧ МЕГА']
fch_m_df = remove_date_duplicates(raw_fch_m_df)




bot = telebot.TeleBot("5278455211:AAFMeE_Y3ifxbILymO_WhmSpYGc0zrkquH8", parse_mode ='None') 

#Через tail
def last_report(df):
    
    if ('Revenue_rent' in df):
        msg2 = ''
        msg = df.tail(1)[[
            'Date','Name','All_revenue', 'Rest_cash']].rename(columns = {
                "Date":"Дата","Name":"Имя","All_revenue":"Выручка",
                "Rest_cash":"В кассе", }) \
        .to_dict('list')
        mk_money = int(df.tail(1)['Revenue_rent'])
        all_money = int(df.tail(1)['All_revenue'])
        mk_percent = round (mk_money*100/all_money, 2)
        msg['Дата'] = msg.get('Дата')[0].date()
        msg['Дата'] = msg.get('Дата').strftime("%d-%m-%Y")
        msg['% Аренда'] = mk_percent
        keys = [*msg]
        for i in range(len(keys)):
            msg2 += str(keys[i])
            msg2 += ' || '  
        msg2  += '\n'
        msg2  += '\n'
        for i in range(len(keys)):
            msg2 += str(msg.get(keys[i]))
            if i < len(keys) - 1:
                msg2 += ' || '
            else:
                msg2 += '%'
            
        msg2 = msg2.replace("'",'')
        msg2 = msg2.replace (']', '')
        msg2 = msg2.replace ('[', '')
        return (msg2)
    elif ('MK_revenue' in df):
        msg2 = ''
        msg = df.tail(1)[[
            'Date','Name','All_revenue', 'Rest_cash']].rename(columns = {
                "Date":"Дата","Name":"Имя","All_revenue":"Выручка",
                "Rest_cash":"В кассе", }) \
        .to_dict('list')
        mk_money = int(df.tail(1)['MK_revenue'])
        all_money = int(df.tail(1)['All_revenue'])
        mk_percent = round (mk_money*100/all_money, 2)
        msg['Дата'] = msg.get('Дата')[0].date()
        msg['Дата'] = msg.get('Дата').strftime("%d-%m-%Y")
        msg['% МК'] = mk_percent
        keys = [*msg]
        for i in range(len(keys)):
            msg2 += str(keys[i])
            msg2 += ' || '  
        msg2  += '\n'
        msg2  += '\n'
        for i in range(len(keys)):
            msg2 += str(msg.get(keys[i]))
            if i < len(keys) - 1:
                msg2 += ' || '
            else:
                msg2 += '%'
            
        msg2 = msg2.replace("'",'')
        msg2 = msg2.replace (']', '')
        msg2 = msg2.replace ('[', '')
        return (msg2)
    
    elif (df.iloc[0]['Shop'] == 'Фраде МЕГА') or (df.iloc[0]['Shop'] == 'Фраде Молл'):
        msg2 = ''
        msg = df.tail(1)[[
            'Date','Name','All_revenue', 'Rest_cash']].rename(columns = {
                "Date":"Дата","Name":"Имя","All_revenue":"Выручка",
                "Rest_cash":"В кассе", }) \
        .to_dict('list')
        
        
        msg['Дата'] = msg.get('Дата')[0].date()
        msg['Дата'] = msg.get('Дата').strftime("%d-%m-%Y")
        
        keys = [*msg]
        for i in range(len(keys)):
            msg2 += str(keys[i])
            msg2 += ' || '  
        msg2  += '\n'
        msg2  += '\n'
        for i in range(len(keys)):
            msg2 += str(msg.get(keys[i]))
            
            msg2 += ' || '
            
            
        msg2 = msg2.replace("'",'')
        msg2 = msg2.replace (']', '')
        msg2 = msg2.replace ('[', '')
        return (msg2)
    
def get_today_report(df):
    today = pd.Timestamp(datetime.date.today())
    #today = pd.Timestamp(datetime.date.today() - datetime.timedelta(16))
    df_wo_dups = remove_date_duplicates(df)
    if df_wo_dups[df_wo_dups['Date'] == today].empty:
                  return ('Сегодняшний отчет еще не загружен')
    else:
        
        raw_data = df_wo_dups.loc[df['Date'] == today,['Date', 'Name', 'All_revenue',
                                                                             'Client_number', 'Rest_cash', 'report_photo']]
    raw_data['Date'] = raw_data['Date'].dt.date
    return (raw_data)    

@bot.message_handler(commands=['start'])
def start(message):     
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=(True))
    btn1 = types.KeyboardButton("Фан Чулан Мега")
    btn2 = types.KeyboardButton("Frade Мега")
    btn3 = types.KeyboardButton("Фан Чулан КМ")
    btn4 = types.KeyboardButton("Атмосфера")
    btn5 = types.KeyboardButton("Frade КМ")
    btn6 = types.KeyboardButton("Все точки")
    btn7 = types.KeyboardButton("Frade")
    btn8 = types.KeyboardButton("Фан Чулан") 
    btn9 = types.KeyboardButton("Общий отчет")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9) 
    bot.send_message(message.chat.id, "Выберете точку", reply_markup = markup)
    
    bot.register_next_step_handler(message, start_reply) 

def start_reply(message):
    if (message.text == "Фан Чулан Мега"):
        k_b = types.ReplyKeyboardMarkup()
        k_b.add(types.KeyboardButton("Последний отчёт"), types.KeyboardButton("Текущая неделя"),
                    types.KeyboardButton("Текущий месяц"), types.KeyboardButton("Отчет по месяцам"))
        
        bot.send_message(message.chat.id, "Выберете дату", reply_markup = k_b)
        bot.register_next_step_handler(message, dates_fchm)


        
    elif message.text == "Frade Мега":
    
        k_b = types.ReplyKeyboardMarkup()
        k_b.add(types.KeyboardButton("Последний отчёт"), types.KeyboardButton("Последние 10 дней"),
                    types.KeyboardButton("Отчет по датам"), types.KeyboardButton("Отчет по месяцам"))
        
        bot.send_message(message.chat.id, "Выберете дату", reply_markup = k_b)
        bot.register_next_step_handler(message, dates_fradem)
        
    elif message.text == "Фан Чулан КМ":
    
        k_b = types.ReplyKeyboardMarkup()
        k_b.add(types.KeyboardButton("Последний отчёт"), types.KeyboardButton("Последние 10 дней"),
                    types.KeyboardButton("Отчет по датам"), types.KeyboardButton("Отчет по месяцам"))
        
        bot.send_message(message.chat.id, "Выберете дату", reply_markup = k_b)
        bot.register_next_step_handler(message, dates_fchkm)
            
    elif message.text == "Атмосфера":
    
        k_b = types.ReplyKeyboardMarkup()
        k_b.add(types.KeyboardButton("Последний отчёт"), types.KeyboardButton("Последние 10 дней"),
                    types.KeyboardButton("Отчет по датам"), types.KeyboardButton("Отчет по месяцам"))
        
        bot.send_message(message.chat.id, "Выберете дату", reply_markup = k_b)
        bot.register_next_step_handler(message, dates_atmo)
            
    elif message.text == "Frade КМ":
    
        k_b = types.ReplyKeyboardMarkup()
        k_b.add(types.KeyboardButton("Последний отчёт"), types.KeyboardButton("Последние 10 дней"),
                    types.KeyboardButton("Отчет по датам"), types.KeyboardButton("Отчет по месяцам"))
        
        bot.send_message(message.chat.id, "Выберете дату", reply_markup = k_b)
        bot.register_next_step_handler(message, dates_fradekm)
            
    elif message.text == "Все точки":
    
        k_b = types.ReplyKeyboardMarkup()
        k_b.add(types.KeyboardButton("Последний отчёт"), types.KeyboardButton("Последние 10 дней"),
                    types.KeyboardButton("Отчет по датам"), types.KeyboardButton("Отчет по месяцам"))
        
        bot.send_message(message.chat.id, "Выберете дату", reply_markup = k_b)
        bot.register_next_step_handler(message, dates_all)
            
    elif message.text == "Frade":
   
        k_b = types.ReplyKeyboardMarkup()
        k_b.add(types.KeyboardButton("Последний отчёт"), types.KeyboardButton("Последние 10 дней"),
                    types.KeyboardButton("Отчет по датам"), types.KeyboardButton("Отчет по месяцам"))
        
        bot.send_message(message.chat.id, "Выберете дату", reply_markup = k_b)
        bot.register_next_step_handler(message, dates_all_frade)
        
    elif message.text == "Фан Чулан":
    
        k_b = types.ReplyKeyboardMarkup()
        k_b.add(types.KeyboardButton("Последний отчёт"), types.KeyboardButton("Последние 10 дней"),
                    types.KeyboardButton("Отчет по датам"), types.KeyboardButton("Отчет по месяцам"))
        
        bot.send_message(message.chat.id, "Выберете дату", reply_markup = k_b)
        bot.register_next_step_handler(message, dates_all_fch)
        
    elif message.text == "Общий отчет":
        pass
                


def dates_fchm (message):
    if (message.text == "Последний отчёт"):
        msg = last_report(fch_m_df)
        bot.send_message(message.chat.id, msg)
       
    elif message.text == "Текущая неделя":
        today = pd.Timestamp.today()
        #Для теста, лень подключать новые файлы.. Пока...
        first_day = '2022-01-12'
        last_day = '2022-01-21'             
# =============================================================================
#         first_day  = today - pd.Timedelta(days = int(today.weekday()))
#         last_day = first_day + pd.Timedelta(days = 6)
# =============================================================================
        #curweek = pd.to_datetime(list(range(0,7)), unit = 'D', origin = first_day)
        out_df = atmosfera_df.copy(deep = True)
        
        out_df = out_df.query("@first_day <= Date <= @last_day")
        out_df['Date'] = out_df['Date'].apply(lambda x: x.strftime("%d-%m-%Y") )
        
        msg = out_df[[
            'Date','Name','All_revenue', 'Rest_cash']].rename(columns = {
                "Date":"Дата","Name":"Имя","All_revenue":"Выручка",
                "Rest_cash":"В кассе", }) \
        .to_dict('list')
        
        
        
        bot.send_message(message.chat.id, msg)
        
   
        
        
    elif message.text == "Отчет по датам":
        pass
    elif message.text == "Отчет по месяцам":
        pass


def dates_fchkm (message):
    if (message.text == "Последний отчёт"):
        msg = last_report(fch_km_df)
        bot.send_message(message.chat.id, msg)
        
    elif message.text == "Последние 10 дней":
        pass
    elif message.text == "Отчет по датам":
        pass
    elif message.text == "Отчет по месяцам":
        pass

def dates_all_fch (message):
    if (message.text == "Последний отчёт"):
        msg1 = last_report(fch_m_df)
        msg2 = last_report(fch_km_df)
        msg =   msg1[:msg1.find('\n')] + '\n' + 'MEGA' +msg1[msg1.find('\n')+1 :] + '\n' + 'KazanMall' \
        + msg2[msg2.find('\n') + 1 :]
        bot.send_message(message.chat.id, msg)
        
        
    elif message.text == "Последние 10 дней":
        pass
    elif message.text == "Отчет по датам":
        pass
    elif message.text == "Отчет по месяцам":
        pass

def dates_atmo (message):
    if (message.text == "Последний отчёт"):
        msg = last_report(atmosfera_df)
        bot.send_message(message.chat.id, msg)
        
        
    elif message.text == "Последние 10 дней":
        pass
    elif message.text == "Отчет по датам":
        pass
    elif message.text == "Отчет по месяцам":
        pass

def dates_fradem (message):
    if (message.text == "Последний отчёт"):
        msg = last_report(frade_m_df)
        bot.send_message(message.chat.id, msg)
        
    elif message.text == "Последние 10 дней":
        pass
    elif message.text == "Отчет по датам":
        pass
    elif message.text == "Отчет по месяцам":
        pass

def dates_fradekm (message):
    if (message.text == "Последний отчёт"):
        msg = last_report(frade_km_df)
        bot.send_message(message.chat.id, msg)
        
    elif message.text == "Последние 10 дней":
        pass
    elif message.text == "Отчет по датам":
        pass
    elif message.text == "Отчет по месяцам":
        pass    

def dates_all_frade (message):
    if (message.text == "Последний отчёт"):
        msg1 = last_report(frade_m_df)
        msg2 = last_report(frade_km_df)
        msg =   msg1[:msg1.find('\n')] + '\n' + 'MEGA' +msg1[msg1.find('\n')+1 :] + '\n' + 'KazanMall' \
        + msg2[msg2.find('\n') + 1 :]
        bot.send_message(message.chat.id, msg)
        
    elif message.text == "Последние 10 дней":
        pass
    elif message.text == "Отчет по датам":
        pass
    elif message.text == "Отчет по месяцам":
        pass
    
def dates_all (message):
    if (message.text == "Последний отчёт"):
        pass
        
    elif message.text == "Последние 10 дней":
        pass
    elif message.text == "Отчет по датам":
        pass
    elif message.text == "Отчет по месяцам":
        pass    
    
        

	
    

    
if __name__ == '__main__':
    bot.infinity_polling()

