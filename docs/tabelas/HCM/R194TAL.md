# R194TAL

## Descrição

BS - Talhões

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFaz | Number(008,0) | Não | Código da Fazenda |
| CodGle | Number(005,0) | Não | Gleba |
| CodTal | Number(004,0) | Não | Talhão |
| DesTal | String(030) | Sim | Descrição |
| FatTal | Number(010,5) | Sim | Fator de Talhão |
| VarTal | String(010) | Sim | Variedade do Talhão |
| AreTal | Number(008,2) | Sim | Área do Talhão |
| EspTal | Number(006,2) | Sim | Espaçamento do Talhão |
| DisTal | Number(007,2) | Sim | Distância do Talhão |
| AnoTal | Number(004,0) | Sim | Ano do Plantio |

---

## Chave Primária

- CodFaz
- CodGle
- CodTal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R194TAL_001

**Tabela:** R194GLE

| Origem | Destino |
|--------|---------|
| CodFaz | CodFaz |
| CodGle | CodGle |

