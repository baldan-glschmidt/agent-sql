# R134DRE

## Descrição

Turmas - Participantes

---

## Resumo

- Campos: 15
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código Turma |
| NumEmp | Number(004,0) | Não | Código da Empresa do Participante |
| TipCol | Number(001,0) | Não | Tipo Colaborador Participante |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador Participante |
| ConEmi | String(001) | Sim | Convite Emitido |
| CerEmi | String(001) | Sim | Certificado Emitido |
| FreEmi | String(001) | Sim | Frequência Emitida |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| CodCcu | String(018) | Sim | Código Centro Custo Contábil |
| DatIns | Date | Sim | Data inscrição do participante |
| DatTer | Date | Sim | Data término do participante |
| LnkEad | String(250) | Sim | Link utilizado pelo participante do ensino a distância |
| DatCon | Date | Sim | Data de conclusão |

---

## Chave Primária

- CodCua
- TmaCua
- NumEmp
- TipCol
- NumCad

---

## Índices

### R134DREIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad

---

## Relacionamentos

### IR_R134DRE_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R134DRE_004

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R134DRE_009

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

