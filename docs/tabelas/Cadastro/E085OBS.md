# E085OBS

## Descrição

Cadastros - Clientes - Observações

---

## Resumo

- Campos: 28
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCli | Number(009,0) | Não | Código do cliente |
| SeqObs | Number(009,0) | Não | Sequência da observação |
| TipObs | String(001) | Não | Tipo da observação |
| ObsCli | String(999) | Não | Descrição da observação |
| ObsUsu | Number(010,0) | Sim | Usuário responsável pelo cadastramento da observação |
| ObsDat | Date | Sim | Data do cadastramento da observação |
| ObsHor | Number(005,0) | Sim | Hora do cadastramento da observação |
| SolObs | String(250) | Sim | Solução/resultado da observação |
| SolUsu | Number(010,0) | Sim | Responsável solução/resultado da observação |
| SolDat | Date | Sim | Data da solução/resultado da observação |
| SolHor | Number(005,0) | Sim | Hora da solução/resultado da observação |
| DatPrx | Date | Sim | Data prevista para o próximo contato |
| SeqCto | Number(005,0) | Sim | Sequência de contato no cadastro de contatos do cliente |
| SitObs | String(001) | Não | Situação da observação do cliente |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o  Palmtop |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o  Palmtop |
| MotObs | Number(006,0) | Sim | Código do motivo da observação |
| SolMot | Number(006,0) | Sim | Código do motivo da solução da observação |
| DatVis | Date | Sim | Data para o contato com o cliente |
| SeqVis | Number(004,0) | Sim | Sequência da visita |
| CliOri | Number(009,0) | Sim | Código do cliente de origem |
| SeqOri | Number(009,0) | Sim | Sequência de origem |
| EmpPed | Number(004,0) | Sim | Código da empresa do pedido |
| FilPed | Number(005,0) | Sim | Código da filial do pedido |
| NumPed | Number(008,0) | Sim | Número do pedido |
| SeqIpd | Number(004,0) | Sim | Sequência de item do pedido |
| VarSer | String(001) | Sim | Indica o tipo de serviço para o Varejo |

---

## Chave Primária

- CodCli
- SeqObs

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E085OBS_000

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

