# R107BTN

## Descrição

Perfil PDI - Botões

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPer | Number(004,0) | Não | Perfil de PDI Web |
| GrpPDI | Number(002,0) | Não | Define o grupo de informações do layout |
| SeqBtn | Number(002,0) | Não | Sequência de apresentação do botão |
| RotBtn | String(050) | Sim | Rótulo do botão |
| ActBtn | Number(001,0) | Sim | Ação executada pelo botão |
| ActReg | Number(003,0) | Sim | Define a Regra executada pelo botão |
| ActMod | String(011) | Sim | Define o modelo de relatório executado pelo botão |

---

## Chave Primária

- CodPer
- GrpPDI
- SeqBtn

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R107BTN_001

**Tabela:** R107GRP

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |
| GrpPDI | GrpPDI |

