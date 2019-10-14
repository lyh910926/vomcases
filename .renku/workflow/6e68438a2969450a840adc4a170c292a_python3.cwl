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
      path: ../../src_py/proc_sce.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_10:
    default: 1
    inputBinding:
      position: 10
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_11:
    default: 1
    inputBinding:
      position: 11
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_12:
    default: 1
    inputBinding:
      position: 12
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_13:
    default: 1
    inputBinding:
      position: 13
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_14:
    default: 1
    inputBinding:
      position: 14
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_15:
    default: 0
    inputBinding:
      position: 15
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_16:
    default: 1
    inputBinding:
      position: 16
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_17:
    default: o
    inputBinding:
      position: 17
      prefix: -e
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_18:
    default:
      class: File
      path: ../../data/DINGO/Ea_howard.txt
    inputBinding:
      position: 18
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_19:
    default: o
    inputBinding:
      position: 19
      prefix: -a
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_2:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.2/sce/sce_out.txt
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
      path: ../../data/DINGO/GPPdaily_howard.txt
    inputBinding:
      position: 20
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_21:
    default: d
    inputBinding:
      position: 21
      prefix: -c
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_22:
    default:
      class: Directory
      listing: []
      path: ../../src/VOM/VOM_Fortran
    inputBinding:
      position: 22
      separate: true
      shellQuote: true
    streamable: false
    type: Directory
  input_23:
    default: 01-01-1980
    inputBinding:
      position: 23
      prefix: -s
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_24:
    default: 21-12-2016
    inputBinding:
      position: 24
      prefix: -e
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_25:
    default: d
    inputBinding:
      position: 25
      prefix: -s
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_26:
    default: 5
    inputBinding:
      position: 26
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_27:
    default: d
    inputBinding:
      position: 27
      prefix: -e
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_28:
    default: 9
    inputBinding:
      position: 28
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_29:
    default: w
    inputBinding:
      position: 29
      prefix: -s
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_3:
    default: data/VOM_output/HowardSprings/freedrainage_cpcff1.2/sce_stats
    inputBinding:
      position: 3
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_30:
    default: 11
    inputBinding:
      position: 30
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_31:
    default: w
    inputBinding:
      position: 31
      prefix: -e
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_32:
    default: 2
    inputBinding:
      position: 32
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_33:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/coreprog.f90
    inputBinding:
      position: 33
      prefix: -c
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_34:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/modules.f90
    inputBinding:
      position: 34
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_35:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/readdata.f90
    inputBinding:
      position: 35
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_36:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/sample.f90
    inputBinding:
      position: 36
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_37:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/sce.f90
    inputBinding:
      position: 37
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_38:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/transpmodel.f90
    inputBinding:
      position: 38
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_39:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/watbal.f90
    inputBinding:
      position: 39
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_4:
    default:
      class: File
      path: ../../work/HowardSprings/freedrainage_cpcff1.2/best_10p/vom_namelist
    inputBinding:
      position: 4
      prefix: -n
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_5:
    default:
      class: Directory
      listing: []
      path: ../../work/HowardSprings/freedrainage_cpcff1.2/best_10p
    inputBinding:
      position: 5
      prefix: -w
      separate: true
      shellQuote: true
    streamable: false
    type: Directory
  input_6:
    default:
      class: File
      path: ../../data/VOM_input/HowardSprings/dailyweather.prn
    inputBinding:
      position: 6
      prefix: -d
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_7:
    default: 10
    inputBinding:
      position: 7
      prefix: -p
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_8:
    default: p
    inputBinding:
      position: 8
      prefix: -o
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_9:
    default: 1
    inputBinding:
      position: 9
      separate: true
      shellQuote: true
    streamable: false
    type: int
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_3)
    streamable: false
    type: Directory
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: $(inputs.input_1)
    entryname: src_py/proc_sce.py
    writable: false
  - entry: $(inputs.input_2)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.2/sce/sce_out.txt
    writable: false
  - entry: $(inputs.input_4)
    entryname: work/HowardSprings/freedrainage_cpcff1.2/best_10p/vom_namelist
    writable: false
  - entry: $(inputs.input_5)
    entryname: work/HowardSprings/freedrainage_cpcff1.2/best_10p
    writable: false
  - entry: $(inputs.input_6)
    entryname: data/VOM_input/HowardSprings/dailyweather.prn
    writable: false
  - entry: $(inputs.input_18)
    entryname: data/DINGO/Ea_howard.txt
    writable: false
  - entry: $(inputs.input_20)
    entryname: data/DINGO/GPPdaily_howard.txt
    writable: false
  - entry: $(inputs.input_22)
    entryname: src/VOM/VOM_Fortran
    writable: false
  - entry: $(inputs.input_33)
    entryname: src/VOM/VOM_Fortran/VOM-code/coreprog.f90
    writable: false
  - entry: $(inputs.input_34)
    entryname: src/VOM/VOM_Fortran/VOM-code/modules.f90
    writable: false
  - entry: $(inputs.input_35)
    entryname: src/VOM/VOM_Fortran/VOM-code/readdata.f90
    writable: false
  - entry: $(inputs.input_36)
    entryname: src/VOM/VOM_Fortran/VOM-code/sample.f90
    writable: false
  - entry: $(inputs.input_37)
    entryname: src/VOM/VOM_Fortran/VOM-code/sce.f90
    writable: false
  - entry: $(inputs.input_38)
    entryname: src/VOM/VOM_Fortran/VOM-code/transpmodel.f90
    writable: false
  - entry: $(inputs.input_39)
    entryname: src/VOM/VOM_Fortran/VOM-code/watbal.f90
    writable: false
successCodes: []
temporaryFailCodes: []
