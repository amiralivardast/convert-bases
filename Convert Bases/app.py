from flask import Flask, render_template, request, redirect

app = Flask(__name__, static_folder='static')

# Function to convert base 16 to bases 10, 2, 8
def convert_base16_to_base10(hex_number):
    try:
        decimal_number = int(hex_number, 16)
        return decimal_number
    except ValueError:
        return None

def convert_base16_to_base2(hex_number):
    try:
        decimal_number = int(hex_number, 16)
        binary_number = bin(decimal_number)[2:]
        return binary_number
    except ValueError:
        return None

def convert_base16_to_base8(hex_number):
    try:
        decimal_number = int(hex_number, 16)
        octal_number = oct(decimal_number)[2:]
        return octal_number
    except ValueError:
        return None

# Function to convert base 10 to bases 16, 2, 8
def convert_base10_to_base16(decimal_number):
    try:
        hexadecimal_number = hex(decimal_number)[2:]
        return hexadecimal_number
    except ValueError:
        return None

def convert_base10_to_base2(decimal_number):
    try:
        binary_number = bin(decimal_number)[2:]
        return binary_number
    except ValueError:
        return None

def convert_base10_to_base8(decimal_number):
    try:
        octal_number = oct(decimal_number)[2:]
        return octal_number
    except ValueError:
        return None

# Function to convert base 2 to bases 16, 10, 8
def convert_base2_to_base16(binary_number):
    try:
        decimal_number = int(binary_number, 2)
        hexadecimal_number = hex(decimal_number)[2:]
        return hexadecimal_number
    except ValueError:
        return None

def convert_base2_to_base10(binary_number):
    try:
        decimal_number = int(binary_number, 2)
        return decimal_number
    except ValueError:
        return None

def convert_base2_to_base8(binary_number):
    try:
        decimal_number = int(binary_number, 2)
        octal_number = oct(decimal_number)[2:]
        return octal_number
    except ValueError:
        return None

# Function to convert base 8 to bases 2 ,10, 16
def convert_base8_to_base2(octal_number):
    try:
        decimal_number = int(octal_number, 8)
        binary_number = bin(decimal_number)[2:]
        return binary_number
    except ValueError:
        return None

def convert_base8_to_base10(octal_number):
    try:
        decimal_number = int(octal_number, 8)
        return decimal_number
    except ValueError:
        return None

def convert_base8_to_base16(octal_number):
    try:
        decimal_number = int(octal_number, 8)
        hexadecimal_number = hex(decimal_number)[2:]
        return hexadecimal_number
    except ValueError:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        # Convert base 16 to bases 8, 2, 10 with their functions
        if 'hex' in request.form:
            Hexadecimal_number = request.form['hex']
            oct_hex = convert_base16_to_base8(Hexadecimal_number)
            bin_hex = convert_base16_to_base2(Hexadecimal_number)
            dec_hex = convert_base16_to_base10(Hexadecimal_number)
        
            if dec_hex is not None and bin_hex is not None and oct_hex is not None:
                return render_template('index.html', octal=oct_hex, binary=bin_hex, decimal=dec_hex)
            else:
                error_message = "Invalid hexadecimal number"
                return render_template('index.html', error=error_message)
            
        # Convert base 10 to bases 8, 2, 16 with their functions
        elif 'dec' in request.form:
            decimal_number = request.form['dec']
            oct_dec = convert_base10_to_base8(int(decimal_number))
            bin_dec = convert_base10_to_base2(int(decimal_number))
            hex_dec = convert_base10_to_base16(int(decimal_number))
        
            if hex_dec is not None and oct_dec is not None and bin_dec is not None:
                hex_dec = hex_dec.upper()
                return render_template('index.html', oct=oct_dec, bin=bin_dec, hex=hex_dec)
            else:
                error_message = "Invalid hexadecimal number"
                return render_template('index.html', error=error_message)
            
        # Convert base 2 to bases 8, 10, 16 with their functions
        elif 'bin' in request.form:
            binary_number = request.form['bin']
            oct_bin = convert_base2_to_base8(binary_number)
            dec_bin = convert_base2_to_base10(binary_number)
            hex_bin = convert_base2_to_base16(binary_number)
        
            if dec_bin is not None and hex_bin is not None and oct_bin is not None:
                hex_bin = hex_bin.upper()
                return render_template('index.html', octa=oct_bin, dec=dec_bin, hexa=hex_bin)
            else:
                error_message = "Invalid hexadecimal number"
                return render_template('index.html', error=error_message)
            
        # Convert base 8 to bases 2, 10, 16 with their functions
        elif 'oct' in request.form:
            octal_number = request.form['oct']
            bin_oct = convert_base8_to_base2(octal_number)
            dec_dec = convert_base8_to_base10(octal_number)
            hex_oct = convert_base8_to_base16(octal_number)
        
            if hex_oct is not None and dec_dec is not None and bin_oct is not None:
                hex_oct = hex_oct.upper()
                return render_template('index.html', binar=bin_oct, deci=dec_dec, hexad=hex_oct)
            else:
                error_message = "Invalid hexadecimal number"
                return render_template('index.html', error=error_message)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)