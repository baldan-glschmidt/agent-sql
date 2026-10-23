# R352FGT

## Descrição

S-5503 - Informações do FGTS por Trabalhador em Processo Trabalhista

---

## Resumo

- Campos: 13
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Tipo de Período Apuração |
| NumPro | String(020) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| CpfTra | Number(011,0) | Não | Número do CPF do trabalhador |
| SeqFgt | Number(002,0) | Não | Sequência informações FGTS |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| RecBas | String(040) | Sim | Número do recibo do arquivo de origem (S-1299) |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição (CNPJ/CPF) - Obsoleto |
| CfjIns | String(014) | Sim | CNPJ Alfanumérico |
| OriPro | Number(001,0) | Sim | Origem do processo/demanda |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- NumPro
- CpfTra
- SeqFgt

---

## Índices

### R352FGTIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
