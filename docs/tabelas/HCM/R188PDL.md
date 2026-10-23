# R188PDL

## Descrição

PLR - Produção do Local

---

## Resumo

- Campos: 26
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodMaq | Number(004,0) | Não | Código da Máquina |
| CodPrd | Number(004,0) | Não | Código do Produto |
| DatPro | Date | Não | Data da Produção |
| HorPro | Number(005,0) | Não | Hora Início da Produção |
| DatFim | Date | Sim | Data Término da Produção |
| HorFim | Number(005,0) | Sim | Hora Término da Produção |
| QtdPro | Number(011,2) | Sim | Quantidade Produzida |
| QtdRej | Number(011,2) | Sim | Quantidade Rejeitada |
| Qtd2Lx | Number(011,2) | Sim | Volume de produtos 2a linha |
| PerRej | Number(011,2) | Sim | % Rejeição |
| ProQua | Number(011,2) | Sim | Produção com Qualidade |
| NroFun | Number(009,0) | Sim | Número de Colaboradores |
| NroAfa | Number(009,0) | Sim | Número de Funcionários Afastados |
| NroEfe | Number(009,0) | Sim | Número de Funcionários Efetivos |
| QhrPrj | Number(010,0) | Sim | Horas Projetadas |
| QhrExt | Number(010,0) | Sim | Horas Extras |
| QhrOci | Number(010,0) | Sim | Horas Ociosas |
| QhrCed | Number(010,0) | Sim | Horas Cedidas |
| QhrRec | Number(010,0) | Sim | Horas Recebidas |
| QhrAju | Number(010,0) | Sim | Absenteísmo Justificado |
| QhrAin | Number(010,0) | Sim | Absenteísmo Injustificado |
| QhrEfe | Number(010,0) | Sim | Horas Efetivas |
| ProHor | Number(011,2) | Sim | Produção Hora |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- CodMaq
- CodPrd
- DatPro
- HorPro

---

## Índices

### R188PDLIndice2

**Tipo:** Não unico

Campos:
- NumLoc

---

## Relacionamentos

### IR_R188PDL_003

**Tabela:** R188MAQ

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TabOrg | TabOrg |
| NumLoc | NumLoc |
| CodMaq | CodMaq |

### IR_R188PDL_004

**Tabela:** R188PRD

| Origem | Destino |
|--------|---------|
| CodPrd | CodPrd |

