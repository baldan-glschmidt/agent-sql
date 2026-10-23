# R070MSR

## Descrição

Mensagem Responsável do Aluno

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
| TipDoc | Number(001,0) | Não | Tipo do Documento do Responsável |
| NumDoc | String(020) | Não | Número do Documento do Responsável |
| DatIni | Date | Não | Data Inicial da Apresentação da Mensagem |
| HorIni | Number(005,0) | Não | Hora Inicial da Apresentação da Mensagem |
| DatFim | Date | Sim | Data Final da Apresentação da Mensagem |
| HorFim | Number(005,0) | Sim | Hora Final da Apresentação da Mensagem |
| QtdMsg | Number(002,0) | Sim | Qtde de Vezes que Será Mostrada a Mensagem nos Coletores |
| MsgAcc | String(032) | Sim | Descrição da Mensagem que Será Mostrada nos Coletores |
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

### IR_R070MSR_001

**Tabela:** R073RES

| Origem | Destino |
|--------|---------|
| TipDoc | TipDoc |
| NumDoc | NumDoc |

