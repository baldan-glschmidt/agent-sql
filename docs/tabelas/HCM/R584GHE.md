# R584GHE

## Descrição

Manutenção do Inventário de Riscos - GHEs

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodInv | Number(007,0) | Não | Código do Inventário de Riscos |
| NumAmb | Number(007,0) | Não | Código do Ambiente de Trabalho |
| DatInv | Date | Não | Data do Inventário de Riscos |
| CodPRA | Number(009,0) | Não | Código do Cadastro do PGR |
| CodGHE | Number(009,0) | Não | Código do GHE - Grupo Homogêneo de Exposição |
| DesAmb | String(8000) | Sim | Descrição do Ambiente |
| ConAmb | String(3000) | Sim | Condições Ambientais |
| MedCon | String(2000) | Sim | Medidas de Controle de Engenharia |
| AtiRis | String(8000) | Sim | Descrição das Atividades de Risco do GHE |

---

## Chave Primária

- CodInv
- NumAmb
- DatInv
- CodPRA
- CodGHE

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
