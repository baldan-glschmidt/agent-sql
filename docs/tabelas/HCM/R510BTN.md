# R510BTN

## Descrição

Currículo Web - Botões

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
| CodPer | Number(003,0) | Não | Código do perfil |
| IdiLay | Number(001,0) | Não | Idioma do layout - define o idioma de apresentação |
| CodBtn | Number(003,0) | Não | Código do botão |
| SeqBtn | Number(003,0) | Sim | Sequência de apresentação do botão |
| RotBtn | String(050) | Sim | Rótulo do botão |
| ActBtn | Number(001,0) | Sim | Ação definida para o botão |
| PosBtn | Number(001,0) | Sim | Posição do botão |

---

## Chave Primária

- CodPer
- IdiLay
- CodBtn

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R510BTN_000

**Tabela:** R510PER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

