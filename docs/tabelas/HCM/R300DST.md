# R300DST

## Descrição

Destinatários de Relatórios - Processos Automáticos

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipPat | Number(002,0) | Não | Tipo do Processo Automático |
| CodPro | Number(003,0) | Não | Código do Processo Automático |
| CodDst | Number(003,0) | Não | Código do Cadastro do Destinatário |
| EmaDst | String(250) | Sim | Email do Destinatário do Relatório |
| CodUsu | Number(010,0) | Sim | Usuário do Destinatário |
| CodPer | Number(010,0) | Sim | Código do Perfil |

---

## Chave Primária

- TipPat
- CodPro
- CodDst

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R300DST_001

**Tabela:** R300PRO

| Origem | Destino |
|--------|---------|
| TipPat | TipPat |
| CodPro | CodPro |

