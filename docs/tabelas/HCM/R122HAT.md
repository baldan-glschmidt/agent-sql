# R122HAT

## Descrição

Termos de Uso e Privacidade - Aceite/Recusa

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro Candidato |
| CodVer | Number(004,0) | Não | Código da Versão dos termos de uso e privacidade |
| EmaEnv | String(001) | Sim | Enviou Email |
| SitHat | Number(001,0) | Sim | Situação da aceitação do termo |
| DatTer | Number(014,6) | Sim | Data e Hora que foi aceito ou recusado o termo. |
| CamAux1 | String(001) | Sim | Campo Auxiliar 1 |
| CamAux2 | Date | Sim | Campo Auxiliar 2 |
| CamAux3 | Number(010,0) | Sim | Campo Auxiliar 3 |

---

## Chave Primária

- NumCan
- CodVer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122HAT_001

**Tabela:** R510TUP

| Origem | Destino |
|--------|---------|
| CodVer | CodVer |

