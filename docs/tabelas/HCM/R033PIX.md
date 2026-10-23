# R033PIX

## Descrição

Pessoa - Pix

---

## Resumo

- Campos: 14
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPes | Number(009,0) | Não | Código da Pessoa |
| DatAlt | Date | Não | Data de Alteração |
| SeqCon | Number(002,0) | Não | Sequência |
| DatAbe | Date | Sim | Data de Abertura |
| DatEnc | Date | Sim | Data de Encerramento |
| EmpAux | Number(004,0) | Sim | USO EXCLUSIVO SENIOR |
| TipAux | Number(001,0) | Sim | USO EXCLUSIVO SENIOR |
| CadAux | Number(009,0) | Sim | USO EXCLUSIVO SENIOR |
| DepAux | Number(002,0) | Sim | USO EXCLUSIVO SENIOR |
| ColAti | Number(001,0) | Sim | USO EXCLUSIVO SENIOR |
| CanAux | Number(007,0) | Sim | USO EXCLUSIVO SENIOR |
| DatAux | Date | Sim | USO EXCLUSIVO SENIOR |
| TpcPix | Number(002,0) | Sim | Tipo de Chave Pix - Pagamento Instantâneo |
| ChvPix | String(100) | Sim | Chave Pix - Pagamento Instantâneo |

---

## Chave Primária

- CodPes
- DatAlt
- SeqCon

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R033PIX_000

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

