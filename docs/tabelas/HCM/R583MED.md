# R583MED

## Descrição

GHE - Revisão do GHE - Laudo - Medições

---

## Resumo

- Campos: 13
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| CodGHE | Number(009,0) | Não | Código do GHE - Grupo Homogêneo de Exposição |
| RevGHE | String(010) | Não | Código da Revisão do GHE |
| CodAgt | Number(006,0) | Não | Código do Perigo/Fator de Risco |
| DatLau | Date | Não | Data da Medição |
| HorIni | Number(005,0) | Não | Hora inicial da medição |
| HorTer | Number(005,0) | Sim | Hora de término da medição |
| QuaAge | Number(011,5) | Sim | Quantificação do perigo/fator de risco |
| QuaAte | Number(011,5) | Sim | Quantificação final do perigo/fator de risco |
| QuaCol | Number(011,5) | Sim | Quantificação perigo/fator de risco considerando fator de redução |
| CodNiv | Number(003,0) | Sim | Código do nível de medição |
| ObsMed | String(2000) | Sim | Observação da Medição |
| CriMed | Number(001,0) | Sim | Critério da medição |

---

## Chave Primária

- CodPRA
- CodGHE
- RevGHE
- CodAgt
- DatLau
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R583MED_003

**Tabela:** R583LAU

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |
| CodGHE | CodGHE |
| RevGHE | RevGHE |
| CodAgt | CodAgt |

