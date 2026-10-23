# R584RIS

## Descrição

Manutenção do Inventário de Riscos - GHEs - Riscos

---

## Resumo

- Campos: 17
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodInv | Number(007,0) | Não | Código do Inventário de Riscos |
| NumAmb | Number(007,0) | Não | Código do Ambiente de Trabalho |
| DatInv | Date | Não | Data do Inventário de Riscos |
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| CodGHE | Number(009,0) | Não | Código do GHE - Grupo Homogêneo de Exposição |
| SeqRis | Number(006,0) | Não | Sequência do risco |
| CodAgt | Number(006,0) | Não | Código do Perigo/Fator de Risco |
| DesRis | String(080) | Sim | Descrição do risco ocupacional |
| ExpRis | String(250) | Sim | Tipo e tempo de exposição ao risco |
| MatRis | Number(006,0) | Sim | Código da técnica utilizada para avaliação do risco |
| NivPro | Number(001,0) | Sim | Nível de probabilidade do risco |
| NivSev | Number(001,0) | Sim | Nível de severidade do risco |
| NivCla | Number(001,0) | Sim | Nível da classificação do risco |
| ClaRis | String(250) | Sim | Comentários sobre a classificação do risco |
| ValRes | Number(004,0) | Sim | Valor do resultado (Probabilidade x Severidade) |
| OutCon | String(8001) | Sim | Outras medidas de controle existentes |
| IntCon | String(050) | Sim | Intensidade/Concentração |

---

## Chave Primária

- CodInv
- NumAmb
- DatInv
- CodPRA
- CodGHE
- SeqRis

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R584RIS_004

**Tabela:** R584GHE

| Origem | Destino |
|--------|---------|
| CodInv | CodInv |
| NumAmb | NumAmb |
| DatInv | DatInv |
| CodPRA | CodPRA |
| CodGHE | CodGHE |

