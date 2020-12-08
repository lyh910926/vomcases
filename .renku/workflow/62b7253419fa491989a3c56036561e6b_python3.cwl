arguments: []
baseCommand:
- python3
class: CommandLineTool
cwlVersion: v1.0
hints: []
inputs:
  input_1:
    default:
      class: File
      path: ../../src_py/gridded_MAP.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_10:
    default:
      class: File
      path: ../../data/Silo_gridded/1988.monthly_rain.nc
    inputBinding:
      position: 10
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_11:
    default:
      class: File
      path: ../../data/Silo_gridded/1989.monthly_rain.nc
    inputBinding:
      position: 11
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_12:
    default:
      class: File
      path: ../../data/Silo_gridded/1990.monthly_rain.nc
    inputBinding:
      position: 12
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_13:
    default:
      class: File
      path: ../../data/Silo_gridded/1991.monthly_rain.nc
    inputBinding:
      position: 13
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_14:
    default:
      class: File
      path: ../../data/Silo_gridded/1992.monthly_rain.nc
    inputBinding:
      position: 14
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_15:
    default:
      class: File
      path: ../../data/Silo_gridded/1993.monthly_rain.nc
    inputBinding:
      position: 15
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_16:
    default:
      class: File
      path: ../../data/Silo_gridded/1994.monthly_rain.nc
    inputBinding:
      position: 16
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_17:
    default:
      class: File
      path: ../../data/Silo_gridded/1995.monthly_rain.nc
    inputBinding:
      position: 17
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_18:
    default:
      class: File
      path: ../../data/Silo_gridded/1996.monthly_rain.nc
    inputBinding:
      position: 18
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_19:
    default:
      class: File
      path: ../../data/Silo_gridded/1997.monthly_rain.nc
    inputBinding:
      position: 19
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_2:
    default:
      class: File
      path: ../../data/Silo_gridded/1980.monthly_rain.nc
    inputBinding:
      position: 2
      prefix: -i
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_20:
    default:
      class: File
      path: ../../data/Silo_gridded/1998.monthly_rain.nc
    inputBinding:
      position: 20
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_21:
    default:
      class: File
      path: ../../data/Silo_gridded/1999.monthly_rain.nc
    inputBinding:
      position: 21
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_22:
    default:
      class: File
      path: ../../data/Silo_gridded/2000.monthly_rain.nc
    inputBinding:
      position: 22
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_23:
    default:
      class: File
      path: ../../data/Silo_gridded/2001.monthly_rain.nc
    inputBinding:
      position: 23
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_24:
    default:
      class: File
      path: ../../data/Silo_gridded/2002.monthly_rain.nc
    inputBinding:
      position: 24
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_25:
    default:
      class: File
      path: ../../data/Silo_gridded/2003.monthly_rain.nc
    inputBinding:
      position: 25
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_26:
    default:
      class: File
      path: ../../data/Silo_gridded/2004.monthly_rain.nc
    inputBinding:
      position: 26
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_27:
    default:
      class: File
      path: ../../data/Silo_gridded/2005.monthly_rain.nc
    inputBinding:
      position: 27
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_28:
    default:
      class: File
      path: ../../data/Silo_gridded/2006.monthly_rain.nc
    inputBinding:
      position: 28
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_29:
    default:
      class: File
      path: ../../data/Silo_gridded/2007.monthly_rain.nc
    inputBinding:
      position: 29
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_3:
    default:
      class: File
      path: ../../data/Silo_gridded/1981.monthly_rain.nc
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_30:
    default:
      class: File
      path: ../../data/Silo_gridded/2008.monthly_rain.nc
    inputBinding:
      position: 30
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_31:
    default:
      class: File
      path: ../../data/Silo_gridded/2009.monthly_rain.nc
    inputBinding:
      position: 31
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_32:
    default:
      class: File
      path: ../../data/Silo_gridded/2010.monthly_rain.nc
    inputBinding:
      position: 32
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_33:
    default:
      class: File
      path: ../../data/Silo_gridded/2011.monthly_rain.nc
    inputBinding:
      position: 33
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_34:
    default:
      class: File
      path: ../../data/Silo_gridded/2012.monthly_rain.nc
    inputBinding:
      position: 34
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_35:
    default:
      class: File
      path: ../../data/Silo_gridded/2013.monthly_rain.nc
    inputBinding:
      position: 35
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_36:
    default:
      class: File
      path: ../../data/Silo_gridded/2014.monthly_rain.nc
    inputBinding:
      position: 36
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_37:
    default:
      class: File
      path: ../../data/Silo_gridded/2015.monthly_rain.nc
    inputBinding:
      position: 37
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_38:
    default:
      class: File
      path: ../../data/Silo_gridded/2016.monthly_rain.nc
    inputBinding:
      position: 38
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_39:
    default:
      class: File
      path: ../../data/Silo_gridded/2017.monthly_rain.nc
    inputBinding:
      position: 39
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_4:
    default:
      class: File
      path: ../../data/Silo_gridded/1982.monthly_rain.nc
    inputBinding:
      position: 4
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_40:
    default: data/Silo_gridded/MAP.ascii
    inputBinding:
      position: 40
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_5:
    default:
      class: File
      path: ../../data/Silo_gridded/1983.monthly_rain.nc
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_6:
    default:
      class: File
      path: ../../data/Silo_gridded/1984.monthly_rain.nc
    inputBinding:
      position: 6
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_7:
    default:
      class: File
      path: ../../data/Silo_gridded/1985.monthly_rain.nc
    inputBinding:
      position: 7
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_8:
    default:
      class: File
      path: ../../data/Silo_gridded/1986.monthly_rain.nc
    inputBinding:
      position: 8
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_9:
    default:
      class: File
      path: ../../data/Silo_gridded/1987.monthly_rain.nc
    inputBinding:
      position: 9
      separate: true
      shellQuote: true
    streamable: false
    type: File
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_40)
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/Silo_gridded
    writable: true
  - entry: $(inputs.input_1)
    entryname: src_py/gridded_MAP.py
    writable: false
  - entry: $(inputs.input_2)
    entryname: data/Silo_gridded/1980.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_3)
    entryname: data/Silo_gridded/1981.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_4)
    entryname: data/Silo_gridded/1982.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_5)
    entryname: data/Silo_gridded/1983.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_6)
    entryname: data/Silo_gridded/1984.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_7)
    entryname: data/Silo_gridded/1985.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_8)
    entryname: data/Silo_gridded/1986.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_9)
    entryname: data/Silo_gridded/1987.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_10)
    entryname: data/Silo_gridded/1988.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_11)
    entryname: data/Silo_gridded/1989.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_12)
    entryname: data/Silo_gridded/1990.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_13)
    entryname: data/Silo_gridded/1991.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_14)
    entryname: data/Silo_gridded/1992.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_15)
    entryname: data/Silo_gridded/1993.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_16)
    entryname: data/Silo_gridded/1994.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_17)
    entryname: data/Silo_gridded/1995.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_18)
    entryname: data/Silo_gridded/1996.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_19)
    entryname: data/Silo_gridded/1997.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_20)
    entryname: data/Silo_gridded/1998.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_21)
    entryname: data/Silo_gridded/1999.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_22)
    entryname: data/Silo_gridded/2000.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_23)
    entryname: data/Silo_gridded/2001.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_24)
    entryname: data/Silo_gridded/2002.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_25)
    entryname: data/Silo_gridded/2003.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_26)
    entryname: data/Silo_gridded/2004.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_27)
    entryname: data/Silo_gridded/2005.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_28)
    entryname: data/Silo_gridded/2006.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_29)
    entryname: data/Silo_gridded/2007.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_30)
    entryname: data/Silo_gridded/2008.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_31)
    entryname: data/Silo_gridded/2009.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_32)
    entryname: data/Silo_gridded/2010.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_33)
    entryname: data/Silo_gridded/2011.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_34)
    entryname: data/Silo_gridded/2012.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_35)
    entryname: data/Silo_gridded/2013.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_36)
    entryname: data/Silo_gridded/2014.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_37)
    entryname: data/Silo_gridded/2015.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_38)
    entryname: data/Silo_gridded/2016.monthly_rain.nc
    writable: false
  - entry: $(inputs.input_39)
    entryname: data/Silo_gridded/2017.monthly_rain.nc
    writable: false
successCodes: []
temporaryFailCodes: []
