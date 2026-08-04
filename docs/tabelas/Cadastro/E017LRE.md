# E017LRE

## Descrição

Tabelas - Configuração de leiaute do Recebimento Eletrônico

---

## Resumo

- Campos: 14
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodLei | Number(009,0) | Não | Código do leiaute |
| CodEmp | Number(004,0) | Não | Código da empresa |
| TipDoe | String(003) | Não | Tipo do documento eletrônico |
| VerLre | String(010) | Não | Versão do leiaute |
| DesLre | String(100) | Não | Descrição do leiaute |
| ObsLre | String(250) | Sim | Observação do leiaute |
| SitLre | String(001) | Não | Situação do leiaute |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E017LREIndice1

**Tipo:** Unico

Campos:
- CodLei
- CodEmp

---

## Relacionamentos

Nenhum relacionamento cadastrado.
