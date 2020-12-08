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
      path: ../../src_py/model_stats.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_10:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/LPJGUESS/daly_river_uncleared/daly_river_uncleared_gpp_eco.txt
    inputBinding:
      position: 10
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_11:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/MAESPA/DalyRiverUncleared_savannas_maespa_simulation.csv
    inputBinding:
      position: 11
      prefix: --maespa
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_12:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/SPAv1/dalyriveruncleared_hourly_outputs.csv
    inputBinding:
      position: 12
      prefix: --spa
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_13:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/CABLE/DalyRiverUncleared_CABLE.nc
    inputBinding:
      position: 13
      prefix: --cable
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_14:
    default: o
    inputBinding:
      position: 14
      prefix: -e
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_15:
    default:
      class: File
      path: ../../data/DINGO/Ea_daly.txt
    inputBinding:
      position: 15
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_16:
    default: o
    inputBinding:
      position: 16
      prefix: -a
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_17:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_daly.txt
    inputBinding:
      position: 17
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_18:
    default: 5
    inputBinding:
      position: 18
      prefix: -s
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_19:
    default: 9
    inputBinding:
      position: 19
      prefix: -e
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_2:
    default:
      class: File
      path: ../../data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 2
      prefix: --vom
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_20:
    default: w
    inputBinding:
      position: 20
      prefix: -s
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_21:
    default: 12
    inputBinding:
      position: 21
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_22:
    default: w
    inputBinding:
      position: 22
      prefix: -e
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_23:
    default: 3
    inputBinding:
      position: 23
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_24:
    default: o
    inputBinding:
      position: 24
      prefix: -p
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_25:
    default:
      class: File
      path: ../../data/fPAR/fpar_daly_v5.txt
    inputBinding:
      position: 25
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_26:
    default: d
    inputBinding:
      position: 26
      prefix: -p
      separate: false
      shellQuote: true
    streamable: false
    type: string
  input_27:
    default:
      class: File
      path: ../../data/fPAR/dates_v5
    inputBinding:
      position: 27
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_28:
    default: data/SavMIP_stats/BESS/DalyUncleared
    inputBinding:
      position: 28
      prefix: --out_bess
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_29:
    default: data/SavMIP_stats/BIOS2/DalyUncleared
    inputBinding:
      position: 29
      prefix: --out_bios2
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_3:
    default:
      class: File
      path: ../../data/emp_benchmarks/emp1_dal
    inputBinding:
      position: 3
      prefix: --emp1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_30:
    default: data/SavMIP_stats/LPJGUESS/DalyUncleared
    inputBinding:
      position: 30
      prefix: --out_lpjguess
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_31:
    default: data/SavMIP_stats/MAESPA/DalyUncleared
    inputBinding:
      position: 31
      prefix: --out_maespa
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_32:
    default: data/SavMIP_stats/SPA/DalyUncleared
    inputBinding:
      position: 32
      prefix: --out_spa
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_33:
    default: data/SavMIP_stats/CABLE/DalyUncleared
    inputBinding:
      position: 33
      prefix: --out_cable
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_34:
    default: data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best
    inputBinding:
      position: 34
      prefix: --out_vom
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_35:
    default: data/emp_benchmarks/stats_emp1/DalyUncleared
    inputBinding:
      position: 35
      prefix: --out_emp1
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_36:
    default: data/emp_benchmarks/stats_emp2/DalyUncleared
    inputBinding:
      position: 36
      prefix: --out_emp2
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_4:
    default:
      class: File
      path: ../../data/emp_benchmarks/emp1_gpp_dal
    inputBinding:
      position: 4
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_5:
    default:
      class: File
      path: ../../data/emp_benchmarks/emp2_dal
    inputBinding:
      position: 5
      prefix: --emp2
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_6:
    default:
      class: File
      path: ../../data/emp_benchmarks/emp2_gpp_dal
    inputBinding:
      position: 6
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_7:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/BESS/DalyRiverUncleared.csv
    inputBinding:
      position: 7
      prefix: --bess
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_8:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/BIOS2/DalyRiverUncleared_ET_GPP.csv
    inputBinding:
      position: 8
      prefix: --bios2
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_9:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/LPJGUESS/daly_river_uncleared/daly_river_uncleared_et_eco.txt
    inputBinding:
      position: 9
      prefix: --lpjguess
      separate: true
      shellQuote: true
    streamable: false
    type: File
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_28)
    streamable: false
    type: Directory
  output_1:
    outputBinding:
      glob: $(inputs.input_29)
    streamable: false
    type: Directory
  output_2:
    outputBinding:
      glob: $(inputs.input_30)
    streamable: false
    type: Directory
  output_3:
    outputBinding:
      glob: $(inputs.input_31)
    streamable: false
    type: Directory
  output_4:
    outputBinding:
      glob: $(inputs.input_32)
    streamable: false
    type: Directory
  output_5:
    outputBinding:
      glob: $(inputs.input_33)
    streamable: false
    type: Directory
  output_6:
    outputBinding:
      glob: $(inputs.input_34)
    streamable: false
    type: Directory
  output_7:
    outputBinding:
      glob: $(inputs.input_35)
    streamable: false
    type: Directory
  output_8:
    outputBinding:
      glob: $(inputs.input_36)
    streamable: false
    type: Directory
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/SavMIP_stats/BESS/DalyUncleared
    writable: true
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/SavMIP_stats/BIOS2/DalyUncleared
    writable: true
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/SavMIP_stats/LPJGUESS/DalyUncleared
    writable: true
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/SavMIP_stats/MAESPA/DalyUncleared
    writable: true
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/SavMIP_stats/SPA/DalyUncleared
    writable: true
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/SavMIP_stats/CABLE/DalyUncleared
    writable: true
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/emp_benchmarks/stats_emp1/DalyUncleared
    writable: true
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/emp_benchmarks/stats_emp2/DalyUncleared
    writable: true
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_stats_best
    writable: true
  - entry: $(inputs.input_1)
    entryname: src_py/model_stats.py
    writable: false
  - entry: $(inputs.input_2)
    entryname: data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_3)
    entryname: data/emp_benchmarks/emp1_dal
    writable: false
  - entry: $(inputs.input_4)
    entryname: data/emp_benchmarks/emp1_gpp_dal
    writable: false
  - entry: $(inputs.input_5)
    entryname: data/emp_benchmarks/emp2_dal
    writable: false
  - entry: $(inputs.input_6)
    entryname: data/emp_benchmarks/emp2_gpp_dal
    writable: false
  - entry: $(inputs.input_7)
    entryname: data/SavMIP_extracted/SavMIP/BESS/DalyRiverUncleared.csv
    writable: false
  - entry: $(inputs.input_8)
    entryname: data/SavMIP_extracted/SavMIP/BIOS2/DalyRiverUncleared_ET_GPP.csv
    writable: false
  - entry: $(inputs.input_9)
    entryname: data/SavMIP_extracted/SavMIP/LPJGUESS/daly_river_uncleared/daly_river_uncleared_et_eco.txt
    writable: false
  - entry: $(inputs.input_10)
    entryname: data/SavMIP_extracted/SavMIP/LPJGUESS/daly_river_uncleared/daly_river_uncleared_gpp_eco.txt
    writable: false
  - entry: $(inputs.input_11)
    entryname: data/SavMIP_extracted/SavMIP/MAESPA/DalyRiverUncleared_savannas_maespa_simulation.csv
    writable: false
  - entry: $(inputs.input_12)
    entryname: data/SavMIP_extracted/SavMIP/SPAv1/dalyriveruncleared_hourly_outputs.csv
    writable: false
  - entry: $(inputs.input_13)
    entryname: data/SavMIP_extracted/SavMIP/CABLE/DalyRiverUncleared_CABLE.nc
    writable: false
  - entry: $(inputs.input_15)
    entryname: data/DINGO/Ea_daly.txt
    writable: false
  - entry: $(inputs.input_17)
    entryname: data/DINGO/GPPdaily_daly.txt
    writable: false
  - entry: $(inputs.input_25)
    entryname: data/fPAR/fpar_daly_v5.txt
    writable: false
  - entry: $(inputs.input_27)
    entryname: data/fPAR/dates_v5
    writable: false
successCodes: []
temporaryFailCodes: []
