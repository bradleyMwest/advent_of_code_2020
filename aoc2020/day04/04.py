import re

field_regex = {}
field_regex['byr'] = "^([0-9]{4})$" #4 digit number
field_regex['iyr'] = "^([0-9]{4})$" #4 digit number
field_regex['eyr'] = "^([0-9]{4})$" #4 digit number
field_regex['hgt'] = "^([0-9]{2,3})(in|cm)$" # 2 or 3 digit number followed by in or cm
field_regex['hcl'] = "^#[a-f,0-9]{6}$" # hash followed by a 6 digit alphanumeric with only lowercase a-f allowed
field_regex['ecl'] = "^((amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth))$" #only one of these 6 options
field_regex['pid'] = "^[0-9]{9}$" #nine digit number
field_regex['cid'] = "" #do nothing

def read_batch(file):
    with open(file, 'r') as f:
        text = f.read()
    passports = text.split('\n\n')
    return passports

def count_valid_passports(passports):
    valid = 0
    for p in passports:
        fields = [x.group() for x in re.finditer('(ecl)|(pid)|(eyr)|(hcl)|(byr)|(iyr)|(hgt)', p)] # check only mandatory fields
        if len(fields) >= 7:
            valid +=1
    return valid

def check_field_values(field):
    key, value = field.split(":")
    valid = 0 
    match = re.search(field_regex[key], value)
    if match is not None:
        if key == 'byr' and int(match.group()) >= 1920 and int(match.group()) <= 2002:
            valid = 1
            
        elif key == 'iyr' and int(match.group()) >= 2010 and int(match.group()) <= 2020:
            valid = 1
            
        elif key == 'eyr' and int(match.group()) >= 2020 and int(match.group()) <= 2030:
            valid = 1
            
        elif key == 'hgt':
            height = int(re.search("^[0-9]{2,3}",value).group())
            if 'in' in value and height >= 59 and height <=76:
                valid = 1
            elif 'cm' in value and height >= 150 and height <=193:
                valid = 1
        
        elif key == 'hcl':
            valid=1      
        elif key == 'ecl':
            valid = 1
        elif key == 'pid':
            valid = 1
    
    return valid

def count_valid_passports_part2(passports, verbose = False):
    valid_passports = 0
    for p in passports:
        fields = [x.group() for x in re.finditer('(ecl)|(pid)|(eyr)|(hcl)|(byr)|(iyr)|(hgt)', p)] # check only mandatory fields
        if len(fields) == 7:
            split_fields = p.replace(' ',',').replace('\n',',').split(',')
            valid_fields = 0
            for field in split_fields:
                if field != "":
                    res = check_field_values(field)
                    valid_fields += res
                if verbose: print(f"{field} is valid {res}")
                
            if verbose: print()
            if valid_fields == len(fields):
                valid_passports +=1
    
    return valid_passports

passports = read_batch('input_04.txt')
# --- part 1 ----
Nvalid = count_valid_passports(passports)

print(f"There are {Nvalid} valid passports in this set")
print()
# --- part 2 ---
Nvalid = count_valid_passports_part2(passports)

print(f"There are {Nvalid} valid passports with all valid fields in this set")
