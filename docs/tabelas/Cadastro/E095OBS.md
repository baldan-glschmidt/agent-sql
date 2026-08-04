# E095OBS

## Descrição

Cadastros - Fornecedores - Observações

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
| CodFor | Number(009,0) | Não | Código do fornecedor |
| SeqObs | Number(009,0) | Não | Sequência da observação |
| TipObs | String(001) | Não | Tipo da observação |
| ObsFor | String(250) | Não | Texto da observação |
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

- CodFor
- SeqObs

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E095OBS_000

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

