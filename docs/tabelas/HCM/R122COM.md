# R122COM

## Descrição

Candidatos Externos - Comunicação

---

## Resumo

- Campos: 13
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro Candidato |
| DatCom | Date | Não | Data da comunicação com o Candidato |
| HorCom | Number(005,0) | Não | Hora da comunicação com o Candidato |
| EnvRec | Number(001,0) | Sim | Tipo de comunicação com o Candidato: Envio ou Recebimento |
| EndNum | String(255) | Sim | Endereço/Número utilizado para a comunicação |
| AssCom | String(100) | Sim | Assunto da comunicação com o Candidato |
| TxtCom | String(40000) | Sim | Texto da comunicação com o Candidato |
| DthEma | Number(014,6) | Sim | Data/Hora que o e-mail for enviado |
| CodUsu | Number(009,0) | Sim | Usuário responsável pelo último registro da comunicação como o Candidato |
| DthMod | Number(014,6) | Sim | Data/Hora da última modificação no registro da comunicação com o Candidato |
| CodRqu | Number(009,0) | Sim | Código da Requisição que a comunicação está vinculada |
| TipCom | Number(001,0) | Sim | Tipo de comunicação realizada com o Candidato |
| CodEEl | Number(004,0) | Sim | Código do tipo de endereço eletrônico |

---

## Chave Primária

- NumCan
- DatCom
- HorCom

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122COM_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

