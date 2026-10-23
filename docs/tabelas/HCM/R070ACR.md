# R070ACR

## Descrição

Alteração de crachás REP

---

## Resumo

- Campos: 16
- Chave Primária: 0 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipOpe | String(001) | Sim | Tipo de operação |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| NumFis | Number(012,0) | Sim | Número físico do crachá |
| TecCra | Number(001,0) | Sim | Tecnologia do crachá |
| DatEnv | Date | Sim | Data de envio ao dispositivo |
| HorEnv | Number(005,0) | Sim | Hora de envio ao dispositivo |
| NumEip | String(015) | Sim | Número do Endereço IP do Coletor |
| StaAtu | Number(001,0) | Sim | Status do Histórico |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |
| IdtPes | String(023) | Sim | Identificador da Pessoa |
| NomFun | String(040) | Sim | Nome do Colaborador |
| NumPis | Number(011,0) | Sim | Número do PIS/PASEP |
| NumCpf | Number(011,0) | Sim | Número do CPF |
| AltBio | Number(001,0) | Sim | Alteração de Biometria |
| RemRep | Number(001,0) | Sim | Remover pessoa REP |
| TipLis | Number(002,0) | Sim | Tipos de Lista |

---

## Chave Primária

Não possui.

---

## Índices

### R070ACRIndice1

**Tipo:** Não unico

Campos:
- TipOpe
- NumEip
- StaAtu

### R070ACRIndice2

**Tipo:** Não unico

Campos:
- NumCra
- NumFis
- NumEip
- TipLis
- StaAtu

---

## Relacionamentos

Nenhum relacionamento cadastrado.
