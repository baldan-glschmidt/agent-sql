# E090OBS

## Descrição

Cadastros - Representantes - Observações

---

## Resumo

- Campos: 12
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRep | Number(009,0) | Não | Código do representante |
| SeqObs | Number(003,0) | Não | Sequência das observações |
| TipObs | String(001) | Não | Tipo da observação |
| ObsRep | String(250) | Não | Texto da observação |
| ObsUsu | Number(010,0) | Sim | Usuário responsável pela entrada da observação |
| ObsDat | Date | Sim | Data da observação |
| ObsHor | Number(005,0) | Sim | Hora da observação |
| SolObs | String(250) | Sim | Solução dada a observação |
| SolUsu | Number(010,0) | Sim | Responsável pela solução da observação |
| SolDat | Date | Sim | Data da solução da observação |
| SolHor | Number(005,0) | Sim | Hora da solução da observação |
| SitObs | String(001) | Não | Situação da observação |

---

## Chave Primária

- CodRep
- SeqObs

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E090OBS_000

**Tabela:** E090REP

| Origem | Destino |
|--------|---------|
| CodRep | CodRep |

