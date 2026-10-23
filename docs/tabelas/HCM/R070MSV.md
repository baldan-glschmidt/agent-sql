# R070MSV

## Descrição

Mensagem para Visitante

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipDoc | Number(001,0) | Não | Tipo do Documento do Visitante |
| NumDoc | String(020) | Não | Número do Documento do Visitante |
| DatIni | Date | Não | Data Inicial da Mensagem |
| HorIni | Number(005,0) | Não | Hora Inicial da Mensagem |
| DatFim | Date | Sim | Data Inicial da Mensagem |
| HorFim | Number(005,0) | Sim | Hora Final da Mensagem |
| QtdMsg | Number(002,0) | Sim | Qtde de Vezes que Será Mostrada a Mensagem nos Relógios |
| MsgAcc | String(032) | Sim | Descrição da Mensagem que Será Mostrada nos Relógios |
| StaAcc | Number(001,0) | Sim | Status da Mensagem |
| CodUsu | Number(009,0) | Sim | Código do usuário que cadastrou a mensagem |

---

## Chave Primária

- TipDoc
- NumDoc
- DatIni
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R070MSV_001

**Tabela:** R090VIS

| Origem | Destino |
|--------|---------|
| TipDoc | TipDoc |
| NumDoc | NumDoc |

