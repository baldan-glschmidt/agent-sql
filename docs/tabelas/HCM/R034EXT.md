# R034EXT

## Descrição

Dados no Exterior

---

## Resumo

- Campos: 16
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| DatIni | Date | Não | Data Início do Endereço no Exterior |
| CodPai | Number(004,0) | Sim | Código do País |
| DesEst | String(040) | Sim | Estado/Província |
| NomCid | String(040) | Sim | Cidade |
| NomBai | String(020) | Sim | Bairro/Distrito |
| CodPos | String(012) | Sim | Código Postal |
| EndRua | String(100) | Sim | Endereço Residencial |
| EndNum | String(006) | Sim | Número |
| EndCpl | String(025) | Sim | Complemento Endereço |
| NumTel | Number(015,0) | Sim | Número do Telefone |
| DatFim | Date | Sim | Data Final do Endereço no Exteriror |
| NifExt | String(030) | Sim | Número de Identificação Fiscal no Exterior |
| IndNif | Number(001,0) | Sim | Indicativo do Número de Identificação Fiscal |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034EXT_002

**Tabela:** R034CPL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

