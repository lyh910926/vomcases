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
      path: ../../data/DINGO/GPPdaily_adelaide.txt
    inputBinding:
      position: 10
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_11:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_daly.txt
    inputBinding:
      position: 11
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_12:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_dry.txt
    inputBinding:
      position: 12
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_13:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_sturt.txt
    inputBinding:
      position: 13
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_14:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 14
      prefix: --pred_cover
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_15:
    default:
      class: File
      path: ../../data/VOM_output/Litchfield/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 15
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_16:
    default:
      class: File
      path: ../../data/VOM_output/AdelaideRiver/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 16
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_17:
    default:
      class: File
      path: ../../data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 17
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_18:
    default:
      class: File
      path: ../../data/VOM_output/DryRiver/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 18
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_19:
    default:
      class: File
      path: ../../data/VOM_output/SturtPlains/freedrainage_cpcff1.0/sce_best/results_daily.txt
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
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/HowardSprings/sce_best/results_daily.txt
    inputBinding:
      position: 20
      prefix: --pres_cover
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_21:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/Litchfield/sce_best/results_daily.txt
    inputBinding:
      position: 21
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_22:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/AdelaideRiver/sce_best/results_daily.txt
    inputBinding:
      position: 22
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_23:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_best/results_daily.txt
    inputBinding:
      position: 23
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_24:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/DryRiver/sce_best/results_daily.txt
    inputBinding:
      position: 24
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_25:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/prescribed_cover/SturtPlains/sce_best/results_daily.txt
    inputBinding:
      position: 25
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_26:
    default: 2002
    inputBinding:
      position: 26
      prefix: --startyear_obs
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_27:
    default: 2016
    inputBinding:
      position: 27
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_28:
    default: 2007
    inputBinding:
      position: 28
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_29:
    default: 2008
    inputBinding:
      position: 29
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_3:
    default:
      class: File
      path: ../../data/DINGO/Ea_litch.txt
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_30:
    default: 2009
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
    default: 2017
    inputBinding:
      position: 32
      prefix: --endyear_obs
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_33:
    default: 2018
    inputBinding:
      position: 33
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_34:
    default: 2008
    inputBinding:
      position: 34
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_35:
    default: 2017
    inputBinding:
      position: 35
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_36:
    default: 2017
    inputBinding:
      position: 36
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_37:
    default: 2009
    inputBinding:
      position: 37
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_38:
    default: 1995
    inputBinding:
      position: 38
      prefix: --startyear_mod
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_39:
    default: 1995
    inputBinding:
      position: 39
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_4:
    default:
      class: File
      path: ../../data/DINGO/Ea_adelaide.txt
    inputBinding:
      position: 4
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_40:
    default: 1995
    inputBinding:
      position: 40
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_41:
    default: 1995
    inputBinding:
      position: 41
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_42:
    default: 1995
    inputBinding:
      position: 42
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_43:
    default: 1995
    inputBinding:
      position: 43
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_44:
    default: 2015
    inputBinding:
      position: 44
      prefix: --endyear_mod
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_45:
    default: 2015
    inputBinding:
      position: 45
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_46:
    default: 2015
    inputBinding:
      position: 46
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_47:
    default: 2015
    inputBinding:
      position: 47
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_48:
    default: 2015
    inputBinding:
      position: 48
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_49:
    default: 2015
    inputBinding:
      position: 49
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_5:
    default:
      class: File
      path: ../../data/DINGO/Ea_daly.txt
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_50:
    default: Howard Springs
    inputBinding:
      position: 50
      prefix: --sites
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_51:
    default: Litchfield
    inputBinding:
      position: 51
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_52:
    default: Adelaide River
    inputBinding:
      position: 52
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_53:
    default: Daly Uncleared
    inputBinding:
      position: 53
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_54:
    default: Dry River
    inputBinding:
      position: 54
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_55:
    default: Sturt Plains
    inputBinding:
      position: 55
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_56:
    default: data/img/9_fluxpartitioning.png
    inputBinding:
      position: 56
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_57:
    default: 15
    inputBinding:
      position: 57
      prefix: --figsize
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_58:
    default: 27
    inputBinding:
      position: 58
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_6:
    default:
      class: File
      path: ../../data/DINGO/Ea_dry.txt
    inputBinding:
      position: 6
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_7:
    default:
      class: File
      path: ../../data/DINGO/Ea_sturt.txt
    inputBinding:
      position: 7
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_8:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_howard.txt
    inputBinding:
      position: 8
      prefix: --ass_obs
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_9:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_litch.txt
    inputBinding:
      position: 9
      separate: true
      shellQuote: true
    streamable: false
    type: File
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_56)
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
    entryname: data/DINGO/Ea_litch.txt
    writable: false
  - entry: $(inputs.input_4)
    entryname: data/DINGO/Ea_adelaide.txt
    writable: false
  - entry: $(inputs.input_5)
    entryname: data/DINGO/Ea_daly.txt
    writable: false
  - entry: $(inputs.input_6)
    entryname: data/DINGO/Ea_dry.txt
    writable: false
  - entry: $(inputs.input_7)
    entryname: data/DINGO/Ea_sturt.txt
    writable: false
  - entry: $(inputs.input_8)
    entryname: data/DINGO/GPPdaily_howard.txt
    writable: false
  - entry: $(inputs.input_9)
    entryname: data/DINGO/GPPdaily_litch.txt
    writable: false
  - entry: $(inputs.input_10)
    entryname: data/DINGO/GPPdaily_adelaide.txt
    writable: false
  - entry: $(inputs.input_11)
    entryname: data/DINGO/GPPdaily_daly.txt
    writable: false
  - entry: $(inputs.input_12)
    entryname: data/DINGO/GPPdaily_dry.txt
    writable: false
  - entry: $(inputs.input_13)
    entryname: data/DINGO/GPPdaily_sturt.txt
    writable: false
  - entry: $(inputs.input_14)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_15)
    entryname: data/VOM_output/Litchfield/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_16)
    entryname: data/VOM_output/AdelaideRiver/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_17)
    entryname: data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_18)
    entryname: data/VOM_output/DryRiver/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_19)
    entryname: data/VOM_output/SturtPlains/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_20)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/HowardSprings/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_21)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/Litchfield/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_22)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/AdelaideRiver/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_23)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/DalyUncleared/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_24)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/DryRiver/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_25)
    entryname: data/VOM_output/additional_analyses/prescribed_cover/SturtPlains/sce_best/results_daily.txt
    writable: false
successCodes: []
temporaryFailCodes: []
