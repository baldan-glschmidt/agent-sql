# R083LAM

## Descrição

PPRA - Laudo - Medições

---

## Resumo

- Campos: 14
- Chave Primária: 0 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| CmpPpa | Date | Sim | Competência do PPRA |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| CodGru | Number(007,0) | Sim | Grupo de Atividades |
| CodAgt | Number(006,0) | Sim | Código do Perigo/Fator de Risco |
| DatLau | Date | Sim | Data do Laudo |
| HorIni | Number(005,0) | Sim | Hora inicial da medição |
| HorTer | Number(005,0) | Sim | Hora de término da medição |
| QuaAge | Number(011,5) | Sim | Quantificação do perigo/fator de risco |
| ObsMed | String(210) | Sim | Observação |
| CodNiv | Number(003,0) | Sim | Código do nível de medição |
| QuaAte | Number(011,5) | Sim | Quantificação final do perigo/fator de risco |
| QuaCol | Number(011,5) | Sim | Quantificação perigo/fator de risco considerando fator de redução |

---

## Chave Primária

Não possui.

---

## Índices

### R083LAMIndice1

**Tipo:** Não unico

Campos:
- NumEmp
- CmpPpa
- TabOrg
- NumLoc
- CodGru
- CodAgt
- DatLau
- HorIni

---

## Relacionamentos

### IR_R083LAM_011

**Tabela:** R083MED

| Origem | Destino |
|--------|---------|
| CodNiv | CodNiv |

