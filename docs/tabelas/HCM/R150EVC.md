# R150EVC

## Descrição

Evidências de Consentimento por Pessoa

---

## Resumo

- Campos: 14
- Chave Primária: 3 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTer | Number(002,0) | Não | Código do termo de consentimento |
| CodVer | Number(004,0) | Não | Código da versão do termo de consentimento |
| IdtPes | String(023) | Não | Identificador da pessoa |
| DatEvc | Date | Sim | Data da evidência de consentimento |
| HorEvc | Number(005,0) | Sim | Hora da evidência de consentimento |
| EmaEnv | String(100) | Sim | E-mail de envio do termo de consentimento |
| CodUsu | Number(010,0) | Não | Código do usuário que registrou a evidência |
| TipPes | Number(001,0) | Não | Tipo de Pessoa da evidência de consentimento |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador |
| TipDoc | Number(001,0) | Sim | Tipo do Documento do Visitante |
| NumDoc | String(020) | Sim | Número do Documento do Visitante |
| AceCon | Number(001,0) | Não | Tipo de aceite do consentimento |

---

## Chave Primária

- CodTer
- CodVer
- IdtPes

---

## Índices

### R150EVCIndice1

**Tipo:** Não unico

Campos:
- CodTer

### R150EVCIndice2

**Tipo:** Não unico

Campos:
- CodTer
- CodVer

---

## Relacionamentos

### IR_R150EVC_000

**Tabela:** R150TER

| Origem | Destino |
|--------|---------|
| CodTer | CodTer |

### IR_R150EVC_001

**Tabela:** R150TUP

| Origem | Destino |
|--------|---------|
| CodTer | CodTer |
| CodVer | CodVer |

