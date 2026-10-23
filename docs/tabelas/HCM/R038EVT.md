# R038EVT

## Descrição

Histórico de Escala de Vale Transporte

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| IniEvt | Date | Não | Data de Início da Escala de Vale Transporte |
| FimEvt | Date | Sim | Data Final da Escala de Vale Transporte |
| EscVtr | Number(005,0) | Sim | Código da Escala do Vale Transporte |
| PonEmb | Number(004,0) | Sim | Ponto de Embarque |
| StaAtu | Number(001,0) | Sim | Status do Histórico |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- IniEvt

---

## Índices

### R038EVTIndice2

**Tipo:** Não unico

Campos:
- StaAtu
- IniEvt

### R038EVTIndice3

**Tipo:** Não unico

Campos:
- StaAtu
- FimEvt

---

## Relacionamentos

### IR_R038EVT_005

**Tabela:** R028EVT

| Origem | Destino |
|--------|---------|
| EscVtr | EscVtr |

