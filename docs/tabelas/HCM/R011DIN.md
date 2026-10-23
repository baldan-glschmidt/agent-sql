# R011DIN

## Descrição

Definição de Fechamento por Banco de Horas na Integração

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PerRef | Date | Não | Competência do Banco de Horas |
| SeqBhr | Number(002,0) | Não | Sequência do Registro |
| AdiAbo | String(001) | Sim | Adiantar Abono (S/N) |
| AbrBhr | String(200) | Sim | Abrangência de Bancos a Serem Abonados |
| PerAbo | Number(003,0) | Sim | Percentual de Abono |
| LimAbo | Number(010,0) | Sim | Limite de Abono no Adiantamento |
| AnuDeb | String(001) | Sim | Anular Débito (S/N) |
| AbrAnu | String(200) | Sim | Abrangência de Bancos a Serem Abonados na Anulação |
| PerBhr | Number(003,0) | Sim | Percentual de Perdão do Banco |
| LimAnu | Number(010,0) | Sim | Limite de Anulação |
| CalPrg | String(001) | Sim | Calcular Prorrogação (S/N) |

---

## Chave Primária

- PerRef
- SeqBhr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
