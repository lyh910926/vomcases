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
    default: p
    inputBinding:
      position: 10
      prefix: -o
      separate: false
      shellQuote: true
    streamable: false
    type: string
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
    default: 1
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
    default: 0
    inputBinding:
      position: 17
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_18:
    default: 1
    inputBinding:
      position: 18
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_19:
    default: o
    inputBinding:
      position: 19
      prefix: -e
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_2:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff0.8/sce/sce_out.txt
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
      path: ../../data/DINGO/Ea_howard.txt
    inputBinding:
      position: 20
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_21:
    default: o
    inputBinding:
      position: 21
      prefix: -a
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_22:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_howard.txt
    inputBinding:
      position: 22
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_23:
    default: d
    inputBinding:
      position: 23
      prefix: -c
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_24:
    default:
      class: Directory
      listing: []
      path: ../../src/VOM/VOM_Fortran
    inputBinding:
      position: 24
      separate: true
      shellQuote: true
    streamable: false
    type: Directory
  input_25:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/coreprog.f90
    inputBinding:
      position: 25
      prefix: -c
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_26:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/modules.f90
    inputBinding:
      position: 26
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_27:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/readdata.f90
    inputBinding:
      position: 27
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_28:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/sample.f90
    inputBinding:
      position: 28
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_29:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/sce.f90
    inputBinding:
      position: 29
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_3:
    default: data/VOM_output/HowardSprings/freedrainage_cpcff0.8/sce_stats
    inputBinding:
      position: 3
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_30:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/transpmodel.f90
    inputBinding:
      position: 30
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_31:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/watbal.f90
    inputBinding:
      position: 31
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_4:
    default: b
    inputBinding:
      position: 4
      prefix: -o
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_5:
    default: data/VOM_output/HowardSprings/freedrainage_cpcff0.8/sce_best
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_6:
    default:
      class: File
      path: ../../work/HowardSprings/freedrainage_cpcff0.8/best/vom_namelist
    inputBinding:
      position: 6
      prefix: -n
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_7:
    default:
      class: Directory
      listing: []
      path: ../../work/HowardSprings/freedrainage_cpcff0.8/best
    inputBinding:
      position: 7
      prefix: -w
      separate: true
      shellQuote: true
    streamable: false
    type: Directory
  input_8:
    default:
      class: File
      path: ../../data/VOM_input/HowardSprings/dailyweather.prn
    inputBinding:
      position: 8
      prefix: -d
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_9:
    default: 10
    inputBinding:
      position: 9
      prefix: -p
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
  output_1:
    outputBinding:
      glob: $(inputs.input_5)
    streamable: false
    type: Directory
permanentFailCodes: []
requirements: []
successCodes: []
temporaryFailCodes: []
