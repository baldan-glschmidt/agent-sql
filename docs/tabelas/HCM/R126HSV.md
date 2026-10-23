# R126HSV

## Descrição

Solicitação de abertura de vaga - Histórico

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSVa | Number(009,0) | Não | Código da solicitação de vaga |
| SeqHSV | Number(003,0) | Não | Sequência de aprovação |
| DthHSV | Number(014,6) | Sim | Data/Hora de criação da Solicitação de abertura de vaga |
| CodUsu | Number(009,0) | Sim | Código do usuário responsável no momento pela solicitação de vaga |
| ObsHSV | String(2000) | Sim | Observações sobre as alterações realizadas na solicitação de vaga |

---

## Chave Primária

- CodSVa
- SeqHSV

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R126HSV_000

**Tabela:** R126SVA

| Origem | Destino |
|--------|---------|
| CodSVa | CodSVa |

