# R003DFA

## Descrição

Dias Facultativos

---

## Resumo

- Campos: 3
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDFa | Number(003,0) | Não | Código da Tabela de Dias Facultativos |
| DesDFa | String(030) | Sim | Descrição da Tabela de Dias Facultativos |
| CodSit | Number(003,0) | Sim | Código da Situação a ser Apurada no Dia Facultativo |

---

## Chave Primária

- CodDFa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R003DFA_002

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| CodSit | CodSit |

