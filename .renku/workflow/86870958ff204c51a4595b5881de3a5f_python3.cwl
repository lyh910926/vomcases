arguments:
- position: 18
  separate: true
  shellQuote: true
  valueFrom: --xloc_title
- position: 21
  separate: true
  shellQuote: true
  valueFrom: --ylim
baseCommand:
- python3
class: CommandLineTool
cwlVersion: v1.0
hints: []
inputs:
  input_1:
    default:
      class: File
      path: ../../src_py/plot_rootzone_states.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_10:
    default: VOM
    inputBinding:
      position: 10
      prefix: --labels
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_11:
    default: red
    inputBinding:
      position: 11
      prefix: --colors
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_12:
    default: '0.20'
    inputBinding:
      position: 12
      prefix: --i_delz
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_13:
    default: 30
    inputBinding:
      position: 13
      prefix: --i_cz
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_14:
    default: 5
    inputBinding:
      position: 14
      prefix: --i_zr
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_15:
    default:
      class: File
      path: ../../data/DINGO_SWS/SWSCon_howard.txt
    inputBinding:
      position: 15
      prefix: --obs_sm
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_16:
    default:
      class: File
      path: ../../work/HowardSprings/freedrainage_cpcff1.0/best/input/pars.txt
    inputBinding:
      position: 16
      prefix: --pars
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_17:
    default: 'True'
    inputBinding:
      position: 17
      prefix: --legend
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_19:
    default: '.12'
    inputBinding:
      position: 19
      prefix: '-0'
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_2:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 2
      prefix: -i
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_20:
    default: 24
    inputBinding:
      position: 20
      prefix: --size_title
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_22:
    default: 5
    inputBinding:
      position: 22
      prefix: '-3'
      separate: false
      shellQuote: true
    streamable: false
    type: int
  input_23:
    default: 0
    inputBinding:
      position: 23
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_24:
    default: 'True'
    inputBinding:
      position: 24
      prefix: --title
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_25:
    default:
      class: File
      path: ../../data/VOM_soils/HowardSprings/soilprofile.par
    inputBinding:
      position: 25
      prefix: --soildata
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_26:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/comp2015/0_benchmark/resultsdaily.txt
    inputBinding:
      position: 26
      prefix: --i2015
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_27:
    default: 15
    inputBinding:
      position: 27
      prefix: --i_cz2015
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_28:
    default: 10
    inputBinding:
      position: 28
      prefix: --i_zr2015
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_29:
    default: '0.065'
    inputBinding:
      position: 29
      prefix: --i_thetar2015
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_3:
    default: 'True'
    inputBinding:
      position: 3
      prefix: --depth
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_30:
    default: '0.41'
    inputBinding:
      position: 30
      prefix: --i_thetas2015
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_31:
    default: '7.5'
    inputBinding:
      position: 31
      prefix: --i_avg2015
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_32:
    default: '1.89'
    inputBinding:
      position: 32
      prefix: --i_nvg2015
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_33:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_best/su_hourly.txt
    inputBinding:
      position: 33
      prefix: --su_hourly
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_34:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/comp2015/0_benchmark/suvechourly.txt
    inputBinding:
      position: 34
      prefix: --su_hourly2015
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_35:
    default: '0.5'
    inputBinding:
      position: 35
      prefix: --i_delz2015
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_36:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/comp2015/0_benchmark/finalbest.txt
    inputBinding:
      position: 36
      prefix: --pars2015
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_37:
    default: 'True'
    inputBinding:
      position: 37
      prefix: --title
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_38:
    default: 18
    inputBinding:
      position: 38
      prefix: --figsize
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_39:
    default: 25
    inputBinding:
      position: 39
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_4:
    default: s
    inputBinding:
      position: 4
      prefix: -y
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_40:
    default: data/img/5_gw_sm_watpot.png
    inputBinding:
      position: 40
      prefix: --outputfile
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_5:
    default: 2002
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_6:
    default: e
    inputBinding:
      position: 6
      prefix: -y
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_7:
    default: 2005
    inputBinding:
      position: 7
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_8:
    default:
      class: File
      path: ../../data/boreholes/RN021012/DataSet
    inputBinding:
      position: 8
      prefix: --obs_gw
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_9:
    default: data/DINCGO_SWS/SWSCon_howard.txt
    inputBinding:
      position: 9
      prefix: --obs_sm
      separate: true
      shellQuote: true
    streamable: false
    type: string
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
    entryname: data/img
    writable: true
  - entry: $(inputs.input_1)
    entryname: src_py/plot_rootzone_states.py
    writable: false
  - entry: $(inputs.input_2)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_8)
    entryname: data/boreholes/RN021012/DataSet
    writable: false
  - entry: $(inputs.input_15)
    entryname: data/DINGO_SWS/SWSCon_howard.txt
    writable: false
  - entry: $(inputs.input_16)
    entryname: work/HowardSprings/freedrainage_cpcff1.0/best/input/pars.txt
    writable: false
  - entry: $(inputs.input_25)
    entryname: data/VOM_soils/HowardSprings/soilprofile.par
    writable: false
  - entry: $(inputs.input_26)
    entryname: data/VOM_output/additional_analyses/comp2015/0_benchmark/resultsdaily.txt
    writable: false
  - entry: $(inputs.input_33)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_best/su_hourly.txt
    writable: false
  - entry: $(inputs.input_34)
    entryname: data/VOM_output/additional_analyses/comp2015/0_benchmark/suvechourly.txt
    writable: false
  - entry: $(inputs.input_36)
    entryname: data/VOM_output/additional_analyses/comp2015/0_benchmark/finalbest.txt
    writable: false
successCodes: []
temporaryFailCodes: []
