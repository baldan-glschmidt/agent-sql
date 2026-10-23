# R352IFT

## Descrição

S-5503 - Informações relativas à matrícula e categoria do trabalhador

---

## Resumo

- Campos: 14
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| NumPro | String(020) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| CpfTra | Number(011,0) | Não | Número do CPF do trabalhador |
| SeqFgt | Number(002,0) | Não | Sequência informações FGTS |
| SeqIft | Number(002,0) | Não | Sequência Informações |
| NumMat | String(030) | Sim | Matrícula atribuída ao trabalhador |
| CodCat | Number(004,0) | Sim | Código da categoria do trabalhador |
| CatOri | Number(004,0) | Sim | Origem do dirigente sindical ou do trabalhador cedido |
| TotFgt | Number(015,2) | Sim | Valor total de FGTS a recolher no processo trabalhista |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição (CNPJ/CPF) - Obsoleto |
| CfjIns | String(014) | Sim | CNPJ Alfanumérico |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- NumPro
- CpfTra
- SeqFgt
- SeqIft

---

## Índices

### R352IFTIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
