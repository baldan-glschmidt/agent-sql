# R513BTN

## Descrição

Gestão de Desempenho - Botões

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPer | Number(004,0) | Não | Perfil do Formulário de Gestão de Desempenho |
| SeqBtn | Number(003,0) | Não | Sequência de apresentação do botão |
| RotBtn | String(050) | Sim | Rótulo do botão |
| BtnGDE | Number(001,0) | Sim | Ação executada pelo botão |
| BtnReg | Number(003,0) | Sim | Define a regra executada pelo botão |
| BtnMod | String(011) | Sim | Define o modelo de relatório executado pelo botão |

---

## Chave Primária

- CodPer
- SeqBtn

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R513BTN_000

**Tabela:** R513PER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

