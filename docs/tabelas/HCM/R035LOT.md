# R035LOT

## Descrição

PPP - Lotação e Atribuição

---

## Resumo

- Campos: 18
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| SeqReg | Number(004,0) | Não | Sequência do registro |
| DatIni | Date | Sim | Data de início da atuação do colaborador |
| DatTer | Date | Sim | Data de término da atuação do colaborador |
| TipIns | Number(001,0) | Sim | Tipo de Inscrição |
| NumCgc | Number(015,0) | Sim | Número da Inscrição - Obsoleto |
| CfjIns | String(014) | Sim | Número da Inscrição |
| NomLoc | String(150) | Sim | Descrição do Local |
| TitCar | String(100) | Sim | Título do Cargo |
| NomFun | String(150) | Sim | Descrição da Função |
| CodCb2 | String(006) | Sim | Cbo do Cargo |
| AprGfi | String(002) | Sim | Descrição da GFIP |
| ObsLot | String(1000) | Sim | Observação da Lotação e Atribuição |
| SitRPP | Number(001,0) | Sim | Situação do Registro |
| IgnReg | String(001) | Sim | Define se o registro será ignorado na emissão do PPP |
| IndCon | String(001) | Sim | Apresenta se o registro está em conflito com outro |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- SeqReg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
