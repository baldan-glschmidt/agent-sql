# R088AUT

## Descrição

Autorização para Habilitação

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EmpCon | Number(004,0) | Não | Código da Empresa do Condutor |
| TClCon | Number(001,0) | Não | Tipo de Colaborador Condutor |
| CadCon | Number(009,0) | Não | Cadastro do Condutor |
| PlaVei | String(010) | Não | Placa do Veículo |
| DatIni | Date | Não | Data Inicial da Autorização |
| DatFim | Date | Sim | Data Final da Autorização |
| EmpAut | Number(004,0) | Sim | Código da Empresa do Autorizador do Agendamento |
| TClAut | Number(001,0) | Sim | Tipo de Colaborador do Autorizador do Agendamento |
| CadAut | Number(009,0) | Sim | Cadastro do Autorizador do Agendamento |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Inseriu na Lista Negra |

---

## Chave Primária

- EmpCon
- TClCon
- CadCon
- PlaVei
- DatIni

---

## Índices

### R088AUTIndice2

**Tipo:** Não unico

Campos:
- EmpCon
- TClCon
- CadCon

### R088AUTIndice3

**Tipo:** Não unico

Campos:
- PlaVei

---

## Relacionamentos

### IR_R088AUT_003

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

