from __future__ import annotations
import random, time, os, sys
try:
  from selenium.webdriver import Chrome, ChromeOptions
  from selenium.webdriver.common.by import By
except Exception:
  os.system('pip install selenium')
  python = sys.executable
  os.execl(python, python, * sys.argv)
from datetime import datetime
from time import gmtime, strftime
now = datetime.now()
print('             ',now)
print('')
print\
("""

 _______  _______  _______  _______ _________ _______ 
(  ____ \(  ____ \(  ___  )(  ____ \\__   __/(  ___  )
| (    \/| (    \/| (   ) || (    \/   ) (   | (   ) |
| (__    | |      | |   | || (_____    | |   | (___) |
|  __)   | |      | |   | |(_____  )   | |   |  ___  |
| (      | |      | |   | |      ) |   | |   | (   ) |
| (____/\| (____/\| (___) |/\____) |___) (___| )   ( |
(_______/(_______/(_______)\_______)\_______/|/     \|
                                                      
                                                      


                    # #### ####
                  ### \/#|### |/####
                 ##\/#/ \||/##/_/##/_#
               ###  \/###|/ \/ # ###
             ##_\_#\_\## | #/###_/_####
            ## #### # \ #| /  #### ##/##
             __#_--###`  |{,###---###-~
                       \ }{
                        }}{
                        }}{
                        {{}
                  , -=-~{ .-^- _
                        `}
                         {

""")
try:
  inp=input('Input Location & press return else press return: ')
except Exception:
  pass
def ecosia():
  while True:
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    #chrome_options.add_argument("start-maximized")
    chrome_options.add_argument('--user-data-dir=./')
    chrome_options.add_argument('--disable-infobars')
    #PATH = "/Users/yourPath/Desktop/chromedriver"
    #driver = webdriver.Chrome(PATH, options=options)
    driver = Chrome(options=chrome_options)
    try:
        #driver.get("https://www.ecosia.org/account/verify?token=099a34a8-c71d-11ee-8cd0-eb24ff60c8d2")
        driver.get("https://www.ecosia.org/search?q="+random.choice(['24%20hour%20plumbers', 'ariel%20and%20satellite%20installation%20', 'accident%20claims', 'accountants', 'advanced%20driving%20instructors', 'african%20restaurants', 'afro%20hair', 'agricultural%20contractors', 'airport%20transfers', 'alloy%20wheel%20refurbishment', 'alloy%20wheel%20repairs', 'alloy%20wheels', 'american%20restaurants', 'architects', 'architectural%20services', 'architecture%20design', 'artificial%20flowers%20and%20plants', 'artificial%20grass', 'arts%20organisations', 'auctioneers%20and%20valuers', 'automatic%20driving%20lessons', 'beauty%20and%20spa', 'babysitters', 'bangladeshi%20restaurants', 'barbers', 'barriers', 'bars%20and%20wine%20bars', 'basement%20conversion', 'bathroom%20design%20and%20installation', 'bathroom%20equipment', 'batteries', 'battery%20servicing', 'battery%20suppliers', 'beauty%20salons', 'beauty%20schools', 'beauty%20treatments', 'bed%20and%20breakfast', 'bed%20shops', 'beekeeping', 'bespoke%20joinery', 'bistros', 'block%20paving', 'blocked%20drains', 'blocked%20toilets', 'boarding%20kennels', 'body%20massage', 'boiler%20engineers', 'boiler%20installations', 'boiler%20replacements', 'boiler%20service%20and%20repair', 'boiler%20spares', 'bookkeeping%20services', 'brakes%20and%20clutches', 'brakes%20repairs', 'breakdown%20recovery', 'bricklayers', 'builders', 'building%20consultants', 'building%20renovations', 'building%20services%20engineering', 'bumper%20repairs', 'burglar%20alarms%20and%20security%20systems', 'business%20advice', 'business%20plans', 'carpet%20and%20upholstery%20cleaners', 'commercial%20vehicle%20hire', 'cabinet%20makers', 'cafes%20and%20coffee%20shops', 'car%20and%20vehicle%20delivery%20services', 'car%20and%20vehicle%20upholsterers', 'car%20and%20vehicle%20valeting', 'car%20accessories%20and%20parts', 'car%20accident%20repairs', 'car%20air%20conditioning', 'car%20body%20repairs', 'car%20brakes', 'car%20breakers', 'car%20diagnostics', 'car%20electrics', 'car%20engine%20tuning%20and%20conversion', 'car%20scratch%20repairs', 'car%20servicing', 'car%20spraying', 'car%20tyres', 'caravan%20parks', 'caribbean%20restaurants', 'carpenters%20and%20joiners', 'carpet%20shops', 'catering%20%20%20food%20and%20drink%20supplies', 'catteries', 'cctv%20installers', 'central%20heating%20equipment', 'central%20heating%20installation', 'central%20heating%20repairs', 'central%20heating%20services', 'charitable%20and%20voluntary%20organisations', 'charity%20shops', 'chauffeur%20driven%20car%20hire', 'childminders%20and%20creches', 'chimney%20repairs', 'chinese%20restaurants', 'civil%20engineers', 'civil%20litigation', 'cladding', 'cleaning%20materials%20and%20supplies', 'clubs%20and%20associations', 'clutch%20repairs', 'coach%20hire', 'cocktail%20bars', 'coffee%20machines%20and%20supplies', 'coffee%20suppliers', 'commercial%20builders', 'commercial%20cleaning', 'commercial%20electricians', 'commercial%20estate%20agents', 'commercial%20plumbers', 'commercial%20vehicle%20parts', 'commercial%20vehicle%20repairs', 'commercial%20waste%20disposal', 'commercial%20wheelie%20bin%20services', 'community%20centres', 'community%20transport', 'company%20formation', 'compensation%20claims', 'computer%20services', 'conference%20facilities%20and%20services', 'conservation%20organisations', 'conservatories', 'conservatory%20cleaning', 'contract%20cleaners', 'conveyancing', 'cooker%20stove%20and%20oven%20repairs%20and%20parts', 'cosmetic%20dentistry', 'cosmetics%20and%20toiletries', 'counselling%20and%20advice', 'crane%20hire', 'criminal%20law', 'curtain%20cleaners', 'dairy%20products', 'damp%20proofing', 'data%20cabling', 'day%20nurseries', 'debt%20advice', 'debt%20management', 'decking', 'deep%20cleaning', 'demolition', 'dent%20removal', 'dental', 'dental%20implants', 'dentists', 'denture%20repairs', 'dentures', 'dermal%20filler%20treatment', 'design', 'discount%20stores', 'distillers', 'divorce%20law', 'diy%20stores', 'doctors%20(medical%20practitioners)', 'dog%20and%20cat%20grooming', 'dog%20day%20care', 'dog%20walking', 'domestic%20cleaning', 'domestic%20electricians', 'domestic%20maintenance%20and%20repair%20services', 'domestic%20waste%20disposal', 'door%20stripping', 'double%20glazed%20windows', 'double%20glazing%20repair', 'drain%20surveys', 'drainage%20consultants', 'drains%20and%20pipe%20cleaning', 'draughting%20services', 'driveway%20cleaning', 'driving%20instructor%20training', 'driving%20schools', 'dry%20cleaners', 'dry%20lining', 'real%20estate', 'electrical%20inspecting%20and%20testing', 'electrical%20installations', 'electrical%20services', 'electricians', 'electrolysis%20and%20laser%20hair%20removal', 'emergency%20dentists', 'emergency%20electricians', 'emergency%20plumbers', 'emergency%20vet', 'employment%20law', 'end%20of%20tenancy%20cleaning', 'energy%20performance%20certificates', 'engine%20diagnostics', 'engine%20reconditioning', 'english%20restaurants', 'equine%20vets', 'equity%20release', 'european%20restaurants', 'exhaust%20systems', 'exterior%20decorating', 'eyelash%20extensions', 'fabric%20and%20haberdashery', 'film%20and%20video%20production%20services', 'food%20and%20drinks', 'facials', 'family%20law', 'farm%20shops', 'farmers', 'fascias%20and%20soffits', 'fast%20food%20restaurants', 'felt%20roofs', 'female%20driving%20instructors', 'fencing%20materials', 'fencing%20services', 'fire%20and%20flood%20restoration', 'fire%20alarm%20servicing', 'fire%20alarms', 'fireplaces', 'firewood', 'fish%20and%20chip%20shops%20and%20restaurants', 'fitted%20bedrooms', 'fitted%20furniture', 'flat%20roof%20repairs', 'floor%20cleaning%20and%20treatment', 'florists', 'florists%20online', 'florists%20supplies', 'flower%20arrangements', 'food%20and%20drink%20%20%20delivered', 'food%20shops', 'forestry%20services', 'french%20restaurants', 'fridge%20and%20freezer%20repairs%20and%20parts', 'function%20rooms%20and%20banqueting', 'fundraising%20services', 'funeral%20flowers', 'furniture%20manufacturers%20and%20designers', 'furniture%20repair%20and%20restoration', 'furniture%20shops', 'garage%20conversions', 'garage%20equipment', 'garage%20services', 'garden%20clearance', 'garden%20designers', 'garden%20drainage', 'garden%20fencing', 'garden%20furniture', 'garden%20maintenance', 'garden%20services', 'gardens', 'gas%20appliances%20retail%20and%20servicing', 'gas%20boilers', 'gas%20central%20heating', 'gas%20cooker%20installation', 'gas%20engineers', 'gas%20fire%20repairs', 'gas%20fires', 'gas%20installers', 'gearboxes', 'glaziers', 'grab%20hire', 'greek%20restaurants', 'greenhouses', 'grocers%20and%20convenience%20stores', 'grounds%20maintenance', 'groundwork%20contractors', 'gum%20treatments', 'gutter%20cleaning', 'guttering%20services', 'health%20and%20wellness%20', 'home%20brew%20shop', 'home%20care%20agency', 'homeopaths', 'hypnotherapy', 'hair%20styling', 'haircuts', 'hairdressers', 'hairdressing%20schools', 'halls', 'handyman%20services', 'hard%20landscaping', 'health%20authorities%20and%20primary%20care%20trusts', 'health%20spas%20and%20resorts', 'heating%20engineers', 'hedge%20cutting', 'high%20pressure%20jetting', 'holiday%20clubs', 'hostels', 'hot%20tubs', 'hotel%20restaurants', 'hotels', 'house%20clearance', 'house%20extensions', 'housing', 'ice%20creams', 'image%20consultants', 'immigration%20advice', 'independent%20schools%20and%20colleges', 'indian%20restaurants', 'indian%20takeaways', 'industrial%20cleaning%20equipment', 'industrial%20heating', 'industrial%20roofing', 'insolvency%20practitioners', 'intensive%20driving%20lessons', 'interior%20designers', 'interior%20landscapers', 'internet%20cafes', 'ironing%20and%20laundry%20services', 'italian%20restaurants', 'job%20interview%20coach', 'janitorial%20supplies', 'japanese%20restaurants', 'joinery%20manufacturers', 'kitchen%20furniture%20suppliers', 'kitchen%20planning%20and%20installation', 'korean%20restaurants', 'lingerie%20', 'ladies%20hairdressers', 'laminate%20floor%20fitters', 'land%20agents', 'landlord%20safety%20certificates', 'landscape%20architects', 'landscapers', 'laptop%20repairs', 'launderettes', 'laundries', 'laundry%20equipment%20and%20supplies', 'lawn%20care', 'lawn%20mowing', 'leadwork', 'lebanese%20restaurants', 'legal%20advice', 'legal%20services', 'letting%20agents', 'lgv%20and%20hgv%20training', 'lifestyle%20management%20and%20concierge%20services', 'limousine%20hire', 'livestock', 'loft%20conversions', 'marketing', 'musical%20instrument%20repair', 'make%20up%20artists', 'malaysian%20restaurants', 'mechanical%20engineers', 'mechanics', 'mediation', 'mediterranean%20restaurants', 'mexican%20restaurants', 'middle%20eastern%20restaurants', 'mineral%20water', 'mini%20buses', 'mini%20cabs', 'mini%20skips', 'minibus%20hire', 'mobile%20auto%20electricians', 'mobile%20beauty%20therapists', 'mobile%20car%20body%20repairs', 'mobile%20hairdressers', 'mobile%20mechanics', 'mobile%20phone%20repairs', 'mobile%20phones%20and%20accessories', 'mobile%20tyre%20fitting', 'mobile%20welders', 'mobility%20bathrooms', 'modern%20cuisine%20restaurants', 'moroccan%20restaurants', 'mortgages', 'mot%20testing', 'motor%20factors', 'motorcycle%20repairs%20and%20services', 'motorcycle%20training%20and%20testing', 'motorcycle%20tyres', 'museums', 'natural%20health%20and%20wellbeing%20specialist', 'night%20club', 'nail%20technicians', 'nails', 'nannies%20and%20au%20pairs', 'nepalese%20restaurants', 'newsagents', 'newspapers%20and%20magazines', 'nhs%20dentistry', 'notaries', 'nursery%20schools', 'off%20licences', 'office%20cleaners', 'office%20fitting%20and%20refurbishment', 'office%20furniture', 'office%20rental', 'oil%20fuel%20distributors%20and%20suppliers', 'oil%20heating%20engineers', 'oil%20tanks', 'orthodontists', 'osteopaths', 'oven%20cleaning', 'overseas%20property', 'private%20tuition%20services', 'painters%20and%20decorators', 'painting%20contractors', 'parking%20sensors', 'part%20worn%20tyres', 'party%20venues', 'party%20wall%20surveyors', 'pass%20plus', 'patio%20cleaning', 'patio%20laying', 'patios', 'paving%20and%20driveways', 'payroll%20services', 'pedicures', 'persian%20restaurants', 'personal%20injury', 'pet%20services', 'pet%20shops', 'pet%20supplies', 'pharmaceutical%20suppliers', 'pharmacies', 'pine%20furniture', 'pizza%20delivery%20and%20takeaway', 'pizzas', 'pizzerias', 'planning%20consultants', 'plants', 'plasterers', 'playgroups%20and%20pre%20school', 'plumbers', 'pointing', 'portuguese%20restaurants', 'poultry%20and%20game%20farmers%20and%20suppliers', 'pressure%20washers', 'principal%20designers', 'private%20dentistry', 'private%20nurseries', 'property%20development', 'property%20for%20sale', 'property%20maintenance', 'property%20management', 'property%20services', 'protective%20coatings', 'pub%20restaurants', 'pubs', 'recording%20engineer', 'recording%20engineers', 'recording%20studio', 'recruitment%20agency', 'removal%20services', 'radiator%20covers', 'rare%20and%20secondhand%20books', 'ready%20mixed%20concrete', 'recycling', 'refresher%20driving%20lessons', 'refurbishment%20commercial%20premises', 'relocation%20agents', 'repointing', 'reproduction%20furniture', 'residential%20and%20retirement%20homes', 'residential%20accommodation', 'residential%20property%20surveyors', 'rewiring', 'riba%20member', 'roof%20cleaning', 'roof%20repairs', 'roof%20tiles', 'roofing%20services', 'root%20canal%20treatment', 'rubbish%20clearance', 'rug%20cleaning', 'russian%20restaurants', 'self%20catering%20holiday%20home', 'shopping', 'shutter%20fitters%20', 'shutter%20suppliers', 'shutters', 'sandwich%20shops', 'sanitary%20hygiene%20services', 'school%20holiday%20clubs', 'scottish%20restaurants', 'scrap%20metal%20merchants', 'seafood%20restaurants', 'secondhand%20clothes', 'secondhand%20furniture', 'security%20fencing', 'septic%20tanks', 'serviced%20apartments', 'sewage%20consultants', 'sheds%20garden%20buildings%20and%20garages', 'shop%20fitters', 'shower%20installation', 'skincare', 'skip%20hire', 'slate%20roofing', 'sofa%20beds%20and%20futons', 'soft%20drink%20suppliers', 'solicitors', 'soundproofing', 'spanish%20restaurants', 'speciality%20restaurants', 'sports%20ground%20contractors', 'staircase%20joinery', 'steakhouse%20restaurants', 'steam%20cleaning', 'steel%20fabrications', 'stone%20cleaners%20and%20restorers', 'storage', 'supermarkets', 'surveyors%20and%20valuers', 'suspended%20ceilings', 'telephone%20answering%20services', 'travel', 'tailor%20alterations', 'takeaway%20food', 'tank%20cleaning%20and%20servicing', 'tanning%20salons', 'tattoo%20removal', 'tax', 'tax%20advisers', 'tax%20returns', 'taxis%20and%20private%20hire%20vehicles', 'tea%20and%20coffee%20specialist%20shops', 'teeth%20whitening', 'thai%20massage', 'thai%20restaurants', 'thatching%20services', 'threading', 'timber%20frame%20buildings', 'timber%20merchants', 'tourist%20attractions', 'trade%20unions', 'traditional%20restaurants', 'tree%20surgeons', 'turf%20and%20soil%20supplies', 'turfing%20services', 'turkish%20restaurants', 'tyre%20dealers', 'tyre%20fitting', 'tyre%20repairs', 'tyres', 'uncategorised', 'utilities', 'underfloor%20heating', 'underpinning', 'unisex%20hairdressers', 'used%20car%20dealers', 'used%20tyres', 'virtual%20receptionists', 'valet%20services', 'vat%20returns', 'vegetarian%20restaurants', 'vehicle%20inspection', 'vending%20machine%20services%20and%20supplies', 'vet%20supplies', 'vets', 'vietnamese%20restaurants', 'wedding%20shop', 'wall%20rendering', 'wall%20tie%20replacement', 'wallpapers%20and%20paints', 'washroom%20services', 'waste%20collection', 'water%20coolers', 'water%20garden%20services', 'waterbeds', 'waxing', 'wedding%20cars', 'wedding%20decorations', 'wedding%20dress%20alterations', 'wedding%20dress%20cleaning', 'wedding%20flowers', 'wedding%20hair%20and%20make%20up', 'wedding%20transport', 'wedding%20venues', 'weed%20control', 'welsh%20restaurants', 'wet%20rooms', 'wheelie%20bin%20cleaning', 'wheels', 'wholesalers', 'wills', 'window%20cleaners', 'window%20tinting', 'windscreens', 'wine%20making%20and%20brewing%20supplies', 'wine%20beer%20spirit%20and%20cider%20suppliers', 'wooden%20furniture', 'wooden%20staircases', 'wooden%20windows', 'youth%20and%20community', 'Electrician', 'Plumber', 'Carpenter', 'HVAC%20Technician', 'Mechanic', 'Construction', 'Elevator%20mechanic', 'Painter', 'Licensed%20Practical%20Nurse', 'Roofer', 'Boilermaker', 'Diesel%20Mechanic', 'Home%20inspector', 'Ironworker', 'Mason', 'Automotive%20Service%20Technician', 'Carpet%20installer', 'Dental%20hygienist', 'Gardener', 'Mechanical%20installer', 'Pipefitter', 'Welder', 'Wind%20Turbine%20Technicians', 'Builder',])+"&addon=chrome&addonversion=6.0.2&method=topbar")
        if not inp =='':
          time.sleep(1)
          search_box = driver.find_element(By.NAME, "q")
          time.sleep(1)
          search_box.send_keys(' '+inp)
          time.sleep(1)
          search_box.submit()
          time.sleep(2)
          driver.save_screenshot('screenshot1.png')
        else:
          time.sleep(5)
    except KeyboardInterrupt:
      print("Recieved an interrupt! Shutting down...")
    except Exception:
      pass
    finally:
      #driver.close()
      driver.quit()
if __name__ == "__main__":
  ecosia()
