# R351INT

## Descrição

S-2500 - eSocial - Processo Trabalhista - Informações relativas ao trabalho intermitente

---

## Resumo

- Campos: 13
- Chave Primária: 9 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| NumPro | String(020) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| CpfTra | Number(011,0) | Não | Número do CPF do trabalhador |
| IdeSeq | Number(005,0) | Não | Sequência parcial |
| SeqPtb | Number(009,0) | Não | Sequência |
| SeqIct | Number(009,0) | Não | Sequência |
| SeqIpb | Number(009,0) | Não | Sequência |
| SeqInt | Number(009,0) | Não | Sequência |
| PerRef | Date | Sim | Informar o mês/ano de referência das informações |
| DiaMes | Number(002,0) | Não | Dia do mês efetivamente trabalhado pelo empregado 	com contrato de trabalho intermitente |
| HorTra | String(004) | Sim | Horas trabalhadas no dia pelo empregado com contrato de trabalho intermitente |
| PIDEXC | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- NumPro
- CpfTra
- IdeSeq
- SeqPtb
- SeqIct
- SeqIpb
- SeqInt

---

## Índices

### R351INTIndice1

**Tipo:** Não unico

Campos:
- PIDEXC

---

## Relacionamentos

### IR_R351INT_007

**Tabela:** R351IPB

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| FilEmp | FilEmp |
| NumPro | NumPro |
| CpfTra | CpfTra |
| IdeSeq | IdeSeq |
| SeqPtb | SeqPtb |
| SeqIct | SeqIct |
| SeqIpb | SeqIpb |

