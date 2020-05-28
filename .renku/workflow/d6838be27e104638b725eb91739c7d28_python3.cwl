arguments:
- position: 52
  separate: true
  shellQuote: true
  valueFrom: --loc_title
baseCommand:
- python3
class: CommandLineTool
cwlVersion: v1.0
hints: []
inputs:
  input_1:
    default:
      class: File
      path: ../../src_py/plot_fluxpartitions.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_10:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_dry.txt
    inputBinding:
      position: 10
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_11:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_sturt.txt
    inputBinding:
      position: 11
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_12:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 12
      prefix: --pred_cover
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_13:
    default:
      class: File
      path: ../../data/VOM_output/AdelaideRiver/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 13
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_14:
    default:
      class: File
      path: ../../data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 14
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_15:
    default:
      class: File
      path: ../../data/VOM_output/DryRiver/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 15
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_16:
    default:
      class: File
      path: ../../data/VOM_output/SturtPlains/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 16
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_17:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/HowardSprings/sce_best/results_daily.txt
    inputBinding:
      position: 17
      prefix: --pres_cover
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_18:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/AdelaideRiver/sce_best/results_daily.txt
    inputBinding:
      position: 18
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_19:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_best/results_daily.txt
    inputBinding:
      position: 19
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_2:
    default:
      class: File
      path: ../../data/DINGO/Ea_howard.txt
    inputBinding:
      position: 2
      prefix: --evap_obs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_20:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/DryRiver/sce_best/results_daily.txt
    inputBinding:
      position: 20
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_21:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/SturtPlains/sce_best/results_daily.txt
    inputBinding:
      position: 21
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_22:
    default: 2002
    inputBinding:
      position: 22
      prefix: --startyear_obs
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_23:
    default: 2007
    inputBinding:
      position: 23
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_24:
    default: 2008
    inputBinding:
      position: 24
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_25:
    default: 2009
    inputBinding:
      position: 25
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_26:
    default: 2009
    inputBinding:
      position: 26
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_27:
    default: 2017
    inputBinding:
      position: 27
      prefix: --endyear_obs
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_28:
    default: 2008
    inputBinding:
      position: 28
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_29:
    default: 2017
    inputBinding:
      position: 29
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_3:
    default:
      class: File
      path: ../../data/DINGO/Ea_adelaide.txt
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_30:
    default: 2017
    inputBinding:
      position: 30
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_31:
    default: 2009
    inputBinding:
      position: 31
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_32:
    default: 1995
    inputBinding:
      position: 32
      prefix: --startyear_mod
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_33:
    default: 1995
    inputBinding:
      position: 33
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_34:
    default: 1995
    inputBinding:
      position: 34
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_35:
    default: 1995
    inputBinding:
      position: 35
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_36:
    default: 1995
    inputBinding:
      position: 36
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_37:
    default: 1995
    inputBinding:
      position: 37
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_38:
    default: 2015
    inputBinding:
      position: 38
      prefix: --endyear_mod
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_39:
    default: 2015
    inputBinding:
      position: 39
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_4:
    default:
      class: File
      path: ../../data/DINGO/Ea_daly.txt
    inputBinding:
      position: 4
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_40:
    default: 2015
    inputBinding:
      position: 40
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_41:
    default: 2015
    inputBinding:
      position: 41
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_42:
    default: 2015
    inputBinding:
      position: 42
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_43:
    default: 2015
    inputBinding:
      position: 43
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_44:
    default: Howard Springs
    inputBinding:
      position: 44
      prefix: --sites
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_45:
    default: Adelaide River
    inputBinding:
      position: 45
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_46:
    default: Daly Uncleared
    inputBinding:
      position: 46
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_47:
    default: Dry River
    inputBinding:
      position: 47
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_48:
    default: Sturt Plains
    inputBinding:
      position: 48
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_49:
    default: data/img/9_fluxpartitioning.png
    inputBinding:
      position: 49
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_5:
    default:
      class: File
      path: ../../data/DINGO/Ea_dry.txt
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_50:
    default: 18
    inputBinding:
      position: 50
      prefix: --figsize
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_51:
    default: 22
    inputBinding:
      position: 51
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_53:
    default: '.2'
    inputBinding:
      position: 53
      prefix: '-0'
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_54:
    default: '1.05'
    inputBinding:
      position: 54
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_6:
    default:
      class: File
      path: ../../data/DINGO/Ea_sturt.txt
    inputBinding:
      position: 6
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_7:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_howard.txt
    inputBinding:
      position: 7
      prefix: --ass_obs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_8:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_adelaide.txt
    inputBinding:
      position: 8
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_9:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_daly.txt
    inputBinding:
      position: 9
      separate: true
      shellQuote: true
    streamable: false
    type: File
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_49)
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
    entryname: src_py/plot_fluxpartitions.py
    writable: false
  - entry: $(inputs.input_2)
    entryname: data/DINGO/Ea_howard.txt
    writable: false
  - entry: $(inputs.input_3)
    entryname: data/DINGO/Ea_adelaide.txt
    writable: false
  - entry: $(inputs.input_4)
    entryname: data/DINGO/Ea_daly.txt
    writable: false
  - entry: $(inputs.input_5)
    entryname: data/DINGO/Ea_dry.txt
    writable: false
  - entry: $(inputs.input_6)
    entryname: data/DINGO/Ea_sturt.txt
    writable: false
  - entry: $(inputs.input_7)
    entryname: data/DINGO/GPPdaily_howard.txt
    writable: false
  - entry: $(inputs.input_8)
    entryname: data/DINGO/GPPdaily_adelaide.txt
    writable: false
  - entry: $(inputs.input_9)
    entryname: data/DINGO/GPPdaily_daly.txt
    writable: false
  - entry: $(inputs.input_10)
    entryname: data/DINGO/GPPdaily_dry.txt
    writable: false
  - entry: $(inputs.input_11)
    entryname: data/DINGO/GPPdaily_sturt.txt
    writable: false
  - entry: $(inputs.input_12)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_13)
    entryname: data/VOM_output/AdelaideRiver/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_14)
    entryname: data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_15)
    entryname: data/VOM_output/DryRiver/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_16)
    entryname: data/VOM_output/SturtPlains/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_17)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/HowardSprings/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_18)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/AdelaideRiver/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_19)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_20)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/DryRiver/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_21)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/SturtPlains/sce_best/results_daily.txt
    writable: false
successCodes: []
temporaryFailCodes: []
