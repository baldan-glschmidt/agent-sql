# R510MSG

## Descrição

Currículo Web - Mensagens

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPer | Number(003,0) | Não | Código do perfil |
| IdiLay | Number(001,0) | Não | Idioma do layout - define o idioma de apresentação |
| CodMsg | Number(003,0) | Não | Código da mensagem |
| TxtMsg | String(300) | Sim | Texto da mensagem |

---

## Chave Primária

- CodPer
- IdiLay
- CodMsg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R510MSG_000

**Tabela:** R510PER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

